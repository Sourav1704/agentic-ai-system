"""
Retriever Agent

Responsibility:
- Retrieve information for a given task.
- Simulate external API/database retrieval.
"""

import asyncio


class Retriever:

    def __init__(self):
        self.name = "Retriever Agent"

    async def retrieve(self, task: str):

        print(f"\n[{self.name}] Started")
        print(f"Task : {task}")

        # Simulate API delay
        await asyncio.sleep(2)

        # Simulate retrieval
        if "European" in task:

            result = {
                "region": "European Union",
                "content": (
                    "The EU AI Act follows a risk-based framework. "
                    "AI systems are classified into unacceptable, "
                    "high, limited, and minimal risk categories."
                )
            }

        elif "US" in task:

            result = {
                "region": "United States",
                "content": (
                    "The United States currently regulates AI using "
                    "sector-specific policies through different agencies."
                )
            }

        else:

            result = {
                "region": "Unknown",
                "content": "No information available."
            }

        print(f"[{self.name}] Completed : {result['region']}")

        return result