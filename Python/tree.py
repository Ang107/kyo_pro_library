# 木に関する処理色々


def get_dis(s: int, g: list[list[int]]) -> list[int]:
    """
    s: スタートの頂点
    g: グラフ
    s からの全頂点への距離のリストを返す。
    """
    from collections import deque

    n = len(g)
    deq = deque([s])
    dis = [-1] * n
    dis[s] = 0
    while deq:
        v = deq.popleft()
        for next in g[v]:
            if dis[next] == -1:
                deq.append(next)
                dis[next] = dis[v] + 1
    return dis


def get_diameter(g: list[list[int]]):
    """
    g: グラフ
    木の直径の長さ，及び直径の端点を返す。
    """
    d = get_dis(0, g)
    u = d.index(max(d))
    d = get_dis(u, g)
    v = d.index(max(d))
    return (d[v], u, v)


def euler_tour(g: list[list[int]], s: int = 0):
    """
    sを根としてオイラーツアーを行う。
    頂点sを根とする木について、頂点iの部分木は、[l[i], r[i])となる。
    vsは訪問順ごとに頂点番号を並べている。
    """
    n = len(g)
    l = [-1] * n
    r = [-1] * n
    order = [-1] * n
    cnt = 0
    st = [~s, s]
    visited = [False] * n
    while st:
        v = st.pop()
        if v < 0:
            r[~v] = cnt
        else:
            if visited[v]:
                continue
            visited[v] = True
            l[v] = cnt
            order[cnt] = v
            for next in g[v]:
                if visited[next] == False:
                    st.append(~next)
                    st.append(next)
            cnt += 1
    return l, r, order


def tree_dp_pretreatment(g: list[list[int]], s: int = 0):
    """
    s: 根
    g: グラフ
    木DPの前処理
    頂点sを根としたときに、子から順に頂点を並べた結果と、
    親 to 子のグラフ
    子 to 親のグラフを返す。
    """
    from collections import deque

    n = len(g)
    order = []
    deq = deque([s])
    visited = [False] * n
    visited[s] = True
    to_child = [[] for _ in range(n)]
    to_pearent = [[] for _ in range(n)]
    while deq:
        v = deq.popleft()
        order.append(v)
        for next in g[v]:
            if visited[next] == False:
                visited[next] = True
                deq.append(next)
                to_child[v].append(next)
                to_pearent[next].append(v)
    order = order[::-1]
    return order, to_child, to_pearent
