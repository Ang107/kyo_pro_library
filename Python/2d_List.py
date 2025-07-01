# 90度右回転させたリストを返す
def list_rotate_R90(l):
    return [list(i) for i in zip(*l[::-1])]


# 90度左回転させたリストを返す
def list_rotate_L90(l):
    return ([list(i) for i in zip(*l)])[::-1]


# 転置
def tenti(l):
    return [list(i) for i in zip(*l)]


# 斜めに取得し、二つのリストを返す
def get_slant(l):
    n = len(l)

    # 右下→左上
    rl_d = [
        [l[max(0, -d) + i][max(0, d) + i] for i in range(n - abs(d))]
        for d in range(1 - n, n)
    ]

    # 左下→右上

    lr_d = [
        [l[max(0, d) + i][min(n + d, n) - i - 1] for i in range(n - abs(d))]
        for d in range(1 - n, n)
    ]

    return rl_d, lr_d
