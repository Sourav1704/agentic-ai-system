"""
Planner Agent

Responsibility:
- Analyze the user's request.
- Dynamically generate an execution plan.
"""


class Planner:

    def __init__(self):
        self.name = "Planner Agent"

    def create_plan(self, user_request: str):

        print(f"\n[{self.name}] Planning started...")

        request = user_request.lower()

        plan = []

        step = 1

        # -----------------------------
        # Research / Retrieve
        # -----------------------------
        if "europe" in request or "eu" in request:

            plan.append({
                "id": step,
                "agent": "Retriever",
                "task": "Collect information about European AI regulations",
                "status": "Pending"
            })

            step += 1

        if "us" in request or "united states" in request or "america" in request:

            plan.append({
                "id": step,
                "agent": "Retriever",
                "task": "Collect information about US AI regulations",
                "status": "Pending"
            })

            step += 1

        # -----------------------------
        # Analysis
        # -----------------------------
        if "compare" in request:

            plan.append({
                "id": step,
                "agent": "Analyzer",
                "task": "Compare retrieved information",
                "status": "Pending"
            })

            step += 1

        # -----------------------------
        # Writing
        # -----------------------------
        if (
            "write" in request
            or "report" in request
            or "blog" in request
            or "article" in request
        ):

            plan.append({
                "id": step,
                "agent": "Writer",
                "task": "Generate final report",
                "status": "Pending"
            })

        print(f"[{self.name}] Created {len(plan)} tasks.")

        return plan