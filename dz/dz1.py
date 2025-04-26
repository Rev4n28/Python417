s = [-2, 3, 8, -11, -4, 6]


def minus(lst):
    if len(lst) == 0:
        return 0
    else:
        if lst[0] < 0:
            return 1 + minus(lst[1:])
        else:
            return minus(lst[1:])


print(minus(s))
