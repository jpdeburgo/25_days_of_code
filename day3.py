import re


def read_input(filename):
    with open(filename, "r") as file:
        return [line for line in file]


def get_multiplications(lines, enable_conditions=False):
    multiplications = []
    for line in lines:
        if enable_conditions:
            multiplications.extend(
                re.findall(r"(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", line)
            )
        else:
            multiplications.extend(re.findall(r"mul\([0-9]+,[0-9]+\)", line))
    return multiplications


def multiply(multiplications):
    results = []
    enabled = True
    for multiplcation in multiplications:
        if multiplcation == "do()":
            enabled = True
        elif multiplcation == "don't()":
            enabled = False
        elif enabled:
            reg = re.search(r"mul\(([0-9]+),([0-9]+)\)", multiplcation)
            nums = int(reg.group(1)), int(reg.group(2))
            results.append(nums[0] * nums[1])
    return results


def calculate(lines, enable_conditions=False):
    multiplications = get_multiplications(lines, enable_conditions)
    results = multiply(multiplications)
    return sum(results)


def main():
    lines = read_input("day3.txt")
    result = calculate(lines, True)
    print(result)


main()
