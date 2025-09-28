import timeit
from collections import Counter
from pathlib import Path
from typing import List


def read_numbers(filepath: Path) -> List[int]:
        list_numbers = []
        with open(filepath, "r", newline="\n") as f:
            for line in f:
                list_numbers.append(int(line))

        return list_numbers

def count_numbers(list_numbers: List[int]) -> int:
    c = Counter(list_numbers)
    return c.most_common(1)[0][0]

def find_most_common_from_file(filepath: Path) -> int:
    list_numbers = read_numbers(filepath)
    return count_numbers(list_numbers)

def main():
    most_common_100 = find_most_common_from_file(Path("100_random_numbers.txt"))
    most_common_10000 = find_most_common_from_file(Path("10000_random_numbers.txt"))
    most_common_1M = find_most_common_from_file(Path("1M_random_numbers.txt"))

    time_100 = timeit.timeit(lambda: find_most_common_from_file(Path("100_random_numbers.txt")), number=1)
    time_10000 = timeit.timeit(lambda: find_most_common_from_file(Path("10000_random_numbers.txt")), number=1)
    time_1M = timeit.timeit(lambda: find_most_common_from_file(Path("1M_random_numbers.txt")), number=1)

    print(f"Most common of 100 random numbers: {most_common_100}, took {time_100} s")
    print(f"Most common of 10000 random numbers: {most_common_10000}, took {time_10000} s")
    print(f"Most common of 1M random numbers: {most_common_1M}, took {time_1M} s")



if __name__ == '__main__':
    main()