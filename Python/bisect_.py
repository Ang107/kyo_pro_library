from bisect import bisect_left, insort_left, bisect_right, insort_right


# lの中でx以下の要素のうちの最大のもの
def le(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx < len(l) and l[idx] == x:
        return x
    elif 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# lの中でx以上の要素のうちの最小のもの
def ge(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx - 1 < len(l) and l[idx - 1] == x:
        return x
    elif 0 <= idx < len(l):
        return l[idx]
    else:
        return None


#  lの中でxより小さい要素のうち最大のもの
def lt(l, x):
    idx = bisect_left(l, x)
    if 0 <= idx - 1 < len(l):
        return l[idx - 1]
    else:
        return None


# lの中でxより大きい要素のうち最小のもの
def gt(l, x):
    idx = bisect_right(l, x)
    if 0 <= idx < len(l):
        return l[idx]
    else:
        return None
