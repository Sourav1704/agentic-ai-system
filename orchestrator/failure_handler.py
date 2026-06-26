"""
Failure Handler

Responsibility:
- Retry failed tasks.
- Handle exceptions gracefully.
- Prevent the pipeline from crashing.
"""

import asyncio


class FailureHandler:

    def __init__(self, max_retries=2):
        self.max_retries = max_retries

    async def execute(self, function, *args):

        retry = 0

        while retry <= self.max_retries:

            try:

                result = await function(*args)

                return result

            except Exception as e:

                retry += 1

                print(f"\n❌ Error : {e}")

                if retry <= self.max_retries:

                    print(f"🔄 Retry {retry}/{self.max_retries}")

                    await asyncio.sleep(1)

                else:

                    print("\n🚫 Task Failed Permanently.")

                    return None