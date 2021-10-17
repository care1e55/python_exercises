from collections import Iterable
from dataclasses import dataclass
from typing import Tuple, List

result = []


@dataclass
class Row:
    num: int
    value: int

    def __str__(self):
        return f'{self.num} {self.value}'

    def __repr__(self):
        return f'{self.num} {self.value}'


def read_input() -> Tuple[int]:
    return tuple(map(int, input().split()))


# def read_input(input_str) -> Tuple[int]:
#     return tuple(map(int, input_str.split()))


def read_rows(rows_num: int):
    return (Row(*read_input()) for _ in range(rows_num))


def print_result() -> None:
    for row in result[::-1]:
        print(row)


def fill_values(start: int, stop: int, fill_value: int = -1) -> None:
    for row_num in range(start, stop, -1):
        result.append(Row(row_num, fill_value))


if __name__ == '__main__':
    start, end, today, rows_num = read_input()
    rows = read_rows(rows_num)

    # start, end, today, rows_num = read_input("11 17 15 2")
    # rows = []
    # rows.append(Row(14, 11))
    # rows.append(Row(12, 10))
    # rows.append(Row(15, 13))
    # rows.append(Row(16, 17))

    today_row = Row(today, -1)
    prev_row = Row(end, -1)
    for i, current_row in enumerate(rows):
        if current_row.num > today_row.num:
            continue
        elif current_row.value == -1:
            continue
        elif prev_row.value == -1:
            fill_values(end, today_row.num)
            fill_values(today_row.num, current_row.num - 1, current_row.value)
            prev_row = current_row
            continue
        elif prev_row.value != -1:
            fill_values(prev_row.num - 1, current_row.num - 1, current_row.value)
            prev_row = current_row
    fill_values(prev_row.num - 1, start - 1)
    print_result()
