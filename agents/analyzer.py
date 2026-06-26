"""
Analyzer Agent

Responsibility:
- Analyze retrieved information.
- Compare different sources.
- Generate a structured summary.
"""


class Analyzer:

    def __init__(self):
        self.name = "Analyzer Agent"

    def analyze(self, eu_data: dict, us_data: dict):

        print(f"\n[{self.name}] Started")

        analysis = {
            "title": "Comparison of AI Regulations",
            "summary": {
                "European Union": eu_data["content"],
                "United States": us_data["content"]
            },
            "differences": [
                "EU follows a comprehensive risk-based AI regulation.",
                "US regulates AI through multiple sector-specific agencies.",
                "EU has a single AI Act while the US has no unified federal AI law."
            ],
            "conclusion": (
                "Both regions aim to promote responsible AI, "
                "but their regulatory strategies are significantly different."
            )
        }

        print(f"[{self.name}] Analysis Completed")

        return analysis