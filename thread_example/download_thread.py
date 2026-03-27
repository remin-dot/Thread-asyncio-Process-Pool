import threading
import time
from typing import List


def download_file(file_name: str) -> None:
    delay = 2
    print(f"[THREAD] Starting download: {file_name}")
    time.sleep(delay)
    print(f"[THREAD] Completed download: {file_name}")


def main() -> None:
    files = ["file1.pdf", "file2.zip", "file3.tar.gz", "file4.iso"]
    threads: List[threading.Thread] = []

    print("Starting thread-based downloads...\n")
    start_time = time.time()

    for file_name in files:
        thread = threading.Thread(target=download_file, args=(file_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    print(f"\nAll downloads completed in {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
