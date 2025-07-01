import math


# 座標上の点を、原点を中心に回転（反時計回り）時計回りはdをマイナスに
def ratate(a, b, d):
    d_rad = math.radians(d)  # 角度法を弧度法に変換
    rotated = (a + b * 1j) * math.e ** (1j * d_rad)
    return rotated.real, rotated.imag


# 三頂点の外積を返す関数
def get_gaiseki(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2)


# 三頂点A,B,Cの角ABCを左回りに見た時の角の大きさが180度未満、180度、180より大きいかを返す
def get_angle_180_more_less_equal(a, b, c):
    gaiseki = get_gaiseki(a, b, c)
    # 180度
    if gaiseki == 0:
        return 0
    # 180度より小さい
    elif gaiseki > 0:
        return 1
    # 180度より大きい
    elif gaiseki < 0:
        return -1


# 三頂点の為す三角形の面積を返す
def get_s(a, b, c):
    return abs(get_gaiseki(a, b, c)) / 2


# 頂点数, P = [(x1,y1),(x2,y2),(x3,y3)...]を順に辿った多角形の面積を返す
def polygon_area(N, P):
    return (
        abs(sum(P[i][0] * P[i - 1][1] - P[i][1] * P[i - 1][0] for i in range(N))) / 2.0
    )
