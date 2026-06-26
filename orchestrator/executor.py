import asyncio

from agents.planner import Planner
from agents.retriever import Retriever
from agents.analyzer import Analyzer
from agents.writer import Writer

from orchestrator.failure_handler import FailureHandler
from orchestrator.batcher import Batcher


class Executor:

    def __init__(self):

        self.planner = Planner()
        self.retriever = Retriever()
        self.analyzer = Analyzer()
        self.writer = Writer()

        self.failure_handler = FailureHandler()
        self.batcher = Batcher(batch_size=2)

    async def execute(self, user_request):

        print("\nStreaming Status")
        print("-" * 60)

        print("Planning task...")

        plan = self.planner.create_plan(user_request)

        if len(plan) == 0:
            print("No tasks generated.")
            return None

        print("✓ Plan Created")

        batches = self.batcher.create_batches(plan)

        retrieved_data = {}
        analysis = None
        article = None

        # -----------------------------
        # Execute each batch
        # -----------------------------
        for batch_number, batch in enumerate(batches, start=1):

            print(f"\n========== Batch {batch_number} ==========")

            retriever_tasks = []

            # -----------------------------
            # Launch Retriever Agents
            # -----------------------------
            for step in batch:

                if step["agent"] == "Retriever":

                    retriever_tasks.append(

                        asyncio.create_task(

                            self.failure_handler.execute(

                                self.retriever.retrieve,

                                step["task"]

                            )

                        )

                    )

            # -----------------------------
            # Wait for all retrievers
            # -----------------------------
            if retriever_tasks:

                retrieval_results = await asyncio.gather(*retriever_tasks)

                for result in retrieval_results:

                    if result is not None:

                        retrieved_data[result["region"]] = result

            # -----------------------------
            # Execute Analyzer / Writer
            # -----------------------------
            for step in batch:

                if step["agent"] == "Analyzer":

                    if (
                        "European Union" in retrieved_data
                        and
                        "United States" in retrieved_data
                    ):

                        print("\nRunning Analyzer...")

                        analysis = self.analyzer.analyze(

                            retrieved_data["European Union"],

                            retrieved_data["United States"]

                        )

                        print("✓ Analysis Completed")

                    else:

                        print("\nAnalyzer skipped.")
                        print("Reason: Insufficient retrieved data.")

                elif step["agent"] == "Writer":

                    if analysis is not None:

                        print("\nRunning Writer...")

                        article = self.writer.write(analysis)

                        print("✓ Report Generated")

                        print(article)

                    else:

                        print("\nWriter skipped.")
                        print("Reason: Analysis not available.")

        print("\n✓ Pipeline Finished")

        return article