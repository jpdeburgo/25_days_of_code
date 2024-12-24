"""
The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that 
are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

-- Part 2 --
Now, the same rules apply as before,
except if removing a single level from 
an unsafe report would make it safe, the report instead counts as safe.
"""


def read_input(filename):
    with open(filename, "r") as f:
        return [list(map(lambda num: int(num), line.strip().split())) for line in f]


def is_safe_report(report, include_index=False):
    increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        if increasing and report[i] >= report[i + 1]:
            return (False, i) if include_index else False
        elif not increasing and report[i] <= report[i + 1]:
            return (False, i) if include_index else False
        elif abs(report[i] - report[i + 1]) > 3:
            return (False, i) if include_index else False
    return True


def is_tolerable_report(report):
    tolerable_report = report.copy()
    strikes = 0
    is_tolerable = is_safe_report(tolerable_report)
    while strikes < 1 and not is_tolerable:
        tolerable_report.pop(is_safe_report(tolerable_report, True)[1])
        is_tolerable = is_safe_report(tolerable_report)
        strikes += 1
    return is_tolerable


def get_safe_reports(reports):
    return [report for report in reports if is_safe_report(report)]


def get_tolerable_reports(reports):
    return [report for report in reports if is_tolerable_report(report)]


def main():
    reports = read_input("day2.txt")
    safe_reports = get_safe_reports(reports)
    tolerable_reports = get_tolerable_reports(reports)
    print(len(safe_reports))
    print(len(tolerable_reports))


main()
