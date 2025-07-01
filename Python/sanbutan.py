def f(m):
    pass


def sanbutansaku_min(l, r):
    # 整数に対する三分探索
    # [l,r]: 定義域
    while r - l > 2:
        m1 = (l * 2 + r) / 3
        m2 = (l + r * 2) / 3
        if f(m1) > f(m2):
            l = m1
        else:
            r = m2
    return l, r


def sanbutansaku_max(l, r):
    # 整数に対する三分探索
    # [l,r]: 定義域
    while r - l > 2:
        m1 = (l * 2 + r) / 3
        m2 = (l + r * 2) / 3
        if f(m1) < f(m2):
            l = m1
        else:
            r = m2
    return l, r


def sanbutansaku_min_float(l, r, eps):
    # 整数に対する三分探索
    # [l,r]: 定義域
    # for _ in range(160):  # ループ数を決め打ち
    while r - l > eps:
        m1 = (l * 2 + r) // 3
        m2 = (l + r * 2) // 3
        if f(m1) > f(m2):
            l = m1
        else:
            r = m2
    return l, r


def sanbutansaku_max_float(l, r, eps):
    # 整数に対する三分探索
    # [l,r]: 定義域
    # for _ in range(160):  # ループ数を決め打ち
    while r - l > eps:
        m1 = (l * 2 + r) // 3
        m2 = (l + r * 2) // 3
        if f(m1) < f(m2):
            l = m1
        else:
            r = m2
    return l, r
