def dijkstra(ed, s):
    """
    ダイクストラ O((N+M) log N)
    負の辺があると適用できない
    (計算量が爆発 or 負の閉路があると無限ループ)
    複数頂点からの最短距離を知りたいときは最初にheapに入れるように改造する
    """
    from heapq import heappop, heappush

    inf = float("inf")
    # 初期化
    n = len(ed)
    dis = [inf] * n
    dis[s] = 0
    heap = [(0, s)]
    # ダイクストラ
    while heap:
        d, v = heappop(heap)
        if d > dis[v]:
            continue
        for next, weight in ed[v]:
            assert weight >= 0  # 負の辺はダメ
            new_d = d + weight
            if new_d < dis[next]:
                dis[next] = new_d
                heappush(heap, (new_d, next))
    return dis


def bellman_ford(
    n: int, edge: list[tuple[int, int, int]], s: int
) -> tuple[bool, list[int]]:
    from collections import deque
    from sys import stderr

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
        list[int]: s->iへの距離の最短の長さ。負の閉路およびそこから延びる頂点は-inf
    """
    inf = float("inf")
    d = [inf] * n  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(n - 1):
        update = False  # 更新が行われたか
        for x, y, z in edge:
            if d[x] == inf:
                continue
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break

    neg_cycle_nodes = []  # 負の閉路やそこから延びる頂点のリスト
    for x, y, z in edge:
        if d[x] == inf:
            continue
        if d[y] > d[x] + z:
            d[y] = d[x] + z
            neg_cycle_nodes.append(y)
    if not neg_cycle_nodes:
        return True, d
    print("負の閉路あり", file=stderr)
    deq = deque(neg_cycle_nodes)
    for v in neg_cycle_nodes:
        d[v] = -inf
    g = [[] for _ in range(n)]
    for x, y, z in edge:
        g[x].append(y)
    while deq:
        v = deq.popleft()
        for next in g[v]:
            if d[next] != -inf:
                deq.append(next)
                d[next] = -inf
    return False, d


def bfs(g: list[list[int]], s: int) -> list[int]:
    """
    普通のBFS
    O(N+M)
    g: 隣接リスト
    s: 始点
    複数頂点からの最短距離を知りたいときは最初にdequeに入れるように改造する
    """
    from collections import deque

    n = len(g)
    dis = [-1] * n
    dis[s] = 0
    deq = deque([s])
    while deq:
        v = deq.popleft()
        for next in g[v]:
            if dis[next] == -1:
                dis[next] = dis[v] + 1
                deq.append(next)
    return dis


def bfs_01(g: list[list[tuple[int, int]]], s: int) -> list[int]:
    """
    01BFS
    O(N+M)
    g: 隣接リスト[(次の頂点, 重み)]
    s: 始点
    重みは (0, 1) のみ許容される
    (0, 2), (0, 3), (0, 99)などはOK
    """
    from collections import deque

    inf = float("inf")
    n = len(g)
    dis = [inf] * n
    dis[s] = 0
    deq = deque([s])
    while deq:
        v = deq.popleft()
        for next, w in g[v]:
            if dis[next] > dis[v] + w:
                if w == 0:
                    dis[next] = dis[v]
                    deq.appendleft(next)
                else:
                    dis[next] = dis[v] + w
                    deq.append(next)
    return dis


def bfs_grid(
    g: list[list[str | int]],
    sx: int,
    sy: int,
    block: list[str | int],
    dxy=((-1, 0), (1, 0), (0, -1), (0, 1)),
) -> list[list[int]]:
    """
    グリッド上のBFS
    O(N+M)
    g: グリッド
    (sx,sy): 始点
    block: 侵入できない座標
    """
    from collections import deque

    h = len(g)
    w = len(g[0])
    dis = [[-1] * w for _ in range(h)]
    dis[sx][sy] = 0
    deq = deque([(sx, sy)])
    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if (
                nx in range(h)
                and ny in range(w)
                and dis[nx][ny] == -1
                and g[nx][ny] not in block
            ):
                dis[nx][ny] = dis[x][y] + 1
                deq.append((nx, ny))
    return dis


def warshall_floyd(g: list[list[tuple[int, int]]]) -> tuple[bool, list[list[int]]]:
    """
    全頂点対の最短距離を計算する
    O(N^3)
    負の閉路があると破綻する。
    負の辺だけならOK。
    returns:
        bool: 負の閉路がないならTrue
        list[list[int]]: 頂点対の最短距離
    """
    from sys import stderr

    n = len(g)
    inf = float("inf")
    dis = [[inf] * n for _ in range(n)]
    for i in range(n):
        for j, w in g[i]:
            dis[i][j] = min(dis[i][j], w)
    for i in range(n):
        dis[i][i] = min(dis[i][i], 0)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    neg_cycle_exist = False
    for v in range(n):
        if dis[v][v] < 0:
            neg_cycle_exist = True
            for i in range(n):
                for j in range(n):
                    if dis[i][v] != inf and dis[v][j] != inf:
                        dis[i][j] = -inf
    print("負の閉路あり", file=stderr)
    return not neg_cycle_exist, dis
