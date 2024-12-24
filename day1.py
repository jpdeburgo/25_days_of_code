import re

"""
Maybe the lists are only off by a small amount!
To find out, pair up the numbers and measure how far apart they are. 
Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; 
you'll need to add up all of those distances. 
For example, if you pair up a 3 from the left list with a 7 from the right list, 
the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
    
"""


def read_input(filename):
    with open(filename, "r") as f:
        return [
            list(map(lambda num: int(num), re.split(r"\s+", line.strip())))
            for line in f
        ]


def get_pairs(numbers_list):
    pairs = {"left": [], "right": []}
    for numbers in numbers_list:
        pairs["left"].append(numbers[0])
        pairs["right"].append(numbers[1])
    return {
        "left": list(sorted(pairs.get("left"))),
        "right": list(sorted(pairs.get("right"))),
    }


def get_distance(number):
    return abs(number[0] - number[1])


def find_distances(left_list, right_list):
    distances = []
    for i in range(len(left_list)):
        distances.append(get_distance((left_list[i], right_list[i])))
    return distances


def get_total_distance(distances):
    return sum(distances)


def get_appearances(pairs):
    appearances = {}
    for num in pairs.get("left"):
        appearances[num] = 0
    for num in pairs.get("right"):
        if num in appearances:
            appearances[num] += 1
    return appearances


def get_similarity_score(pairs):
    apperances = get_appearances(pairs)
    score = 0

    for num, count in apperances.items():
        score += count * num
    return score


def main():
    numbers = read_input("day1-input.txt")
    pairs = get_pairs(numbers)
    distances = find_distances(pairs.get("left"), pairs.get("right"))
    total_distance = get_total_distance(distances)
    similarity_score = get_similarity_score(pairs)
    print(f"\n\ntotal_distance: {total_distance}\n\n")
    print(f"\n\nsimilarity_score: {similarity_score}\n\n")


main()
