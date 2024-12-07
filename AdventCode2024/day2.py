import numpy as np
from utils import read_row_file

def main():
    """Day 2: Red-Nosed Reports.

    Puzzle input: consists of many reports, one report per line.
    Each report is a list of numbers called levels that are separated by spaces.
    The engineers are trying to figure out which reports are safe.
    """
    reports = read_row_file('input2.txt', int)

    nb_total_okay, not_okay = day2_part1(reports)
    day2_part2(nb_total_okay, not_okay)


def day2_part1(reports):
    """
    So, a report only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    """
    nb_total_ok = 0
    not_okay = []

    for report in reports:
        ind = 1
        okay = 0
        
        # Check if it is increasing or decreasing
        increasing = all(i < j for i, j in zip(report, report[1:]))
        decreasing = all(i > j for i, j in zip(report, report[1:]))

        if increasing or decreasing:

            # Check range of difference
            while ind < len(report):
                current_level = report[ind - 1]
                next_level = report[ind]
                abs_difference = abs(current_level - next_level)

                # Check if difference is between expected range
                if (abs_difference > 0) & (abs_difference < 4):
                    okay = 1
                    ind += 1
                else:
                    okay = 0
                    not_okay.append(report)
                    break
            
            nb_total_ok += okay

        else:
            not_okay.append(report)
    
    print(f"Part 1 - total ok reports", nb_total_ok)

    return nb_total_ok, not_okay


def check_range(report, ind, bad_level):
    current_level = report[ind - 1]
    next_level = report[ind]
    abs_difference = abs(current_level - next_level)

    # Check if difference is between expected range
    if (abs_difference > 0) & (abs_difference < 4) & (bad_level < 2):
        return 1
    return 0


def check_order(report):
    # Ascending
    if report == sorted(report, reverse=False):
        return "Ascending"
    # Descending
    elif report == sorted(report, reverse=True):
        return "Descending"
    else:
        return "Neither"


def is_safe(row):
    # This calculates the differences between consecutive elements in the row.
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]

    # This checks if all values in inc belong entirely to {1, 2, 3} (positive, small differences)
    # or to {-1, -2, -3} (negative, small differences).
    # If this condition holds, the row is considered "safe."
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}


def day2_part2(nb_total_ok, reports):
    """
    Tolerates a single bad level in what would otherwise be a safe report.

    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe,
    the report instead counts as safe.
    """
    # Iterates over each element's index in the row, temporarily removing the element at index i to create a modified version of the row
    # This combines the sub-list before i with the sub-list after i
    # [1, 2, 3, 4] -> [2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]
    # Differences for [2, 3, 4]: [1, 1] → Safe.
    safe_count = sum(any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports)

    nb_total_ok += safe_count

    # not_okay = []
    # for report in reports:
    #     ind = 1
    #     okay = 0
    #     bad_level = 0

    #     og_report = report.copy()
        
    #     while ind < len(report):
    #         # Check range of difference
    #         okay = check_range(report, ind, bad_level)
    #         if not okay:
    #             bad_level += 1
    #             report.pop(ind - 1)
    #             okay = check_range(report, ind - 1, bad_level)

    #             if bad_level > 1:
    #                 break
    #         ind += 1

    #     # Check ascending/descending

        # if not okay:
        #     not_okay.append(og_report)
        # # else:
        # #     print(og_report, report)
        # nb_total_ok += okay

    print(f"Part 2 - total ok reports", nb_total_ok)


if __name__ == '__main__':
    main()
