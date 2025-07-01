def bellman_ford(
    n: int, edge: list[tuple[int, int, int]], s: int
) -> tuple[bool, list[int]]:
    """
    ベルマンフォードで単一始点からの任意地点までの最短距離を計算する(O(NM))
    頂点に重みがあったときに、頂点対の重みの差の制約からその制約を満たす解を求められる。
    負の閉路がある場合は、解なしを示す。
    Args
        n: 頂点数
        edge: (i, j, k)
            i -> j の辺の長さがk
            edge: w[j] <= w[i] + k を意味する制約
        s: 開始する頂点のインデックス
    Return
        bool: 負の閉路が無い: True, 負の閉路がある: False
        list[int]: s->iへの距離の最短の長さ
    """
    d = [float("inf")] * n  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(n):
        update = False  # 更新が行われたか
        for x, y, z in edge:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return False, d
    return True, d
