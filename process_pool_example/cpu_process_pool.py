import sys
import time
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(0)


def calculate_factorial(n: int) -> int:
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    numbers = [5000, 6000, 5500, 6500, 5200, 6200]

    print("Starting process pool CPU-bound calculations...\n")
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(calculate_factorial, numbers))

    elapsed = time.time() - start_time

    print(f"\nFactorial calculations completed in {elapsed:.2f} seconds")
    for num, result in zip(numbers, results):
        print(f"factorial({num}) = {result} (last 10 digits: {str(result)[-10:]})")


if __name__ == "__main__":
    main()
