import asyncio
import time
from typing import List


async def fetch_data(task_name: str, delay: float) -> str:
    print(f"[ASYNCIO] Starting fetch: {task_name}")
    await asyncio.sleep(delay)
    print(f"[ASYNCIO] Completed fetch: {task_name}")
    return f"Data from {task_name}"


async def main() -> None:
    tasks_config = [
        ("API_1", 1.5),
        ("API_2", 2.0),
        ("API_3", 1.2),
        ("API_4", 1.8),
    ]

    print("Starting async-based data fetching...\n")
    start_time = time.time()

    tasks = [fetch_data(name, delay) for name, delay in tasks_config]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"\nAll fetches completed in {elapsed:.2f} seconds")
    print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
