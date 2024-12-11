import re

from utils import read_row_file

def main():
    """Day 3: Mull It Over.

    The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted.
    It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y).
    However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored.

    For example, consider the following section of corrupted memory:

        xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    Only the four sections are real mul instructions.
    Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
    """
    corrupted_memory = read_row_file('input3.txt', str)
    concat_memory = []
    for line in corrupted_memory:
        concat_memory.extend(line)
    concat_memory = "".join(concat_memory)

    day3_part1(concat_memory)
    day3_part2(concat_memory)


def calculate_total(multipliers):
    total_multiplications = 0
    for mult in multipliers:
        to_multiply = re.findall(r"\d+", mult)
        total_multiplications += int(to_multiply[0]) * int(to_multiply[1])
    return total_multiplications


def day3_part1(concat_memory):
    """
    """
    multipliers = re.findall(r"(mul\(\d+\,\d+\))", concat_memory)
    total_multiplications = calculate_total(multipliers)
    
    print("Day 3 - Part 1: result of the multiplications:", total_multiplications)
        

def day3_part2(concat_memory):
    """There are two new instructions you'll need to handle:

    - The do() instruction enables future mul instructions.
    - The don't() instruction disables future mul instructions.

    Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
    """
    multipliers = re.findall(r"(mul\(\d+\,\d+\)|don't\(\)|do\(\))", concat_memory)
    valid_multipliers = []
    valid = 1
    for mult in multipliers:
        if mult == "don't()":
            valid = 0
        elif mult == "do()":
            valid = 1
        else:
            if valid:
                valid_multipliers.append(mult)

    total_multiplications = calculate_total(valid_multipliers)
    print("Day 3 - Part 2: result of the multiplications:", total_multiplications)


if __name__ == '__main__':
    main()
