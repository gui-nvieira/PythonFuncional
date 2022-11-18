from itertools import dropwhile


def dropWhileEx():
    return list(dropwhile(lambda n: n > 0, [6, 4, 2, 0, -2, -4]))


if __name__ == "__main__":
    print(dropWhileEx())
