import asyncio

from orchestrator.executor import Executor


async def main():

    print("=" * 70)
    print("        Agentic AI Multi-Step Task System")
    print("=" * 70)

    user_request = input(
        "\nEnter your request:\n> "
    )

    executor = Executor()

    await executor.execute(
        user_request
    )


if __name__ == "__main__":

    asyncio.run(main())