"""
Writer Agent

Responsibility:
- Generate the final report/article.
- Convert structured analysis into human-readable content.
"""


class Writer:

    def __init__(self):
        self.name = "Writer Agent"

    def write(self, analysis):

        print(f"\n[{self.name}] Started")

        article = f"""
==============================================================
                 FINAL REPORT
==============================================================

Title:
{analysis["title"]}

--------------------------------------------------------------
SUMMARY
--------------------------------------------------------------

European Union
--------------
{analysis["summary"]["European Union"]}

United States
-------------
{analysis["summary"]["United States"]}

--------------------------------------------------------------
KEY DIFFERENCES
--------------------------------------------------------------
"""

        for i, difference in enumerate(analysis["differences"], start=1):
            article += f"{i}. {difference}\n"

        article += f"""

--------------------------------------------------------------
CONCLUSION
--------------------------------------------------------------

{analysis["conclusion"]}

==============================================================
Generated Successfully by Writer Agent
==============================================================
"""

        print(f"[{self.name}] Report Generated Successfully")

        return article