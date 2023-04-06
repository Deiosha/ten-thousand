import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
        roll 6 standard 6 sided dice, and return 6 values in between 1 - 6.
        :param n: dice rolled
        :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
        """
        return tuple(random.randint(1, 6) for _ in range(n))

    # def calculate_score(roll):
    """
    :param roll:
    :return:
    """

    # score = 0
    # count_pair = 0
    # count = Counter(roll).most_common()
    # num = len(count)
    # # for num in range(0, len(count)):
    # return tuple(random.randint(1, 6) for _ in range(roll))

    def calculate_score(t):
        if len(t) == 1:
            if t[0] == 5:
                return 50
            else:
                return t[0] * 100
        elif len(set(t)) == 1:
            return len(t) * t[0] * 1000
        elif set(t) == {2}:
            return len(t) * 200
        elif set(t) == {3}:
            return len(t) * 300
        elif set(t) == {4}:
            return len(t) * 400
        elif set(t) == {6}:
            return len(t) * 600
        elif set(t) == {1, 2, 3, 4, 5, 6} and sorted(t) == [1, 2, 3, 4, 5, 6]:
            return 1500
        else:
            return 0

        # generate a tuple of six random integers in the range 1-6

    t = tuple(random.randint(1, 6) for i in range(6))

    # calculate the value of the tuple using the calculate_value() function
    value = calculate_score(t)

    # print the tuple and its corresponding value
    print(f"Tuple: {t}")
    print(f"Value: {value}")


if __name__ == "__main__":
    print(GameLogic.roll_dice(6))
