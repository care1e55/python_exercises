import math
import sys

sys.setrecursionlimit(2147483647)


def plintus(denominations, target):
    cache = {}
    if len(denominations) == 0:
        return 0
    if target == 0:
        return 0

    def subproblem(i, t):
        if (i, t) in cache:
            return cache[(i, t)]

        val = denominations[i]
        if val > t:
            choice_take = math.inf
        elif val == t:
            choice_take = 1
        else:
            choice_take = 1 + subproblem(i, t - val)
        choice_leave = (
            math.inf if i == 0
            else subproblem(i - 1, t))
        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        return optimal

    return subproblem(len(denominations) - 1, target)


try:
    upper_bound, target = tuple(map(int, input().split()))
    denominations = list(range(1, upper_bound + 1))
    print(plintus(denominations, target))
except:
    print(0)
