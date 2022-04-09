import itertools


def perms():
    for perm in sorted(list(itertools.permutations(input()))):
        print("".join(perm))


if __name__ == '__main__':
    perms()
