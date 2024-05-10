from bisect import bisect_left, insort_left, bisect_right, insort_right


# 以下
def le(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx < len(l) and l[idx] == x:
        return x
    elif 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# 以上
def ge(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx - 1 < len(l) and l[idx - 1] == x:
        return x
    elif 0 <= idx < len(l):
        return l[idx]
    else:
        return None


# より小さい
def lt(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# より大きい
def gt(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx < len(l):
        return l[idx]
    else:
        return None
