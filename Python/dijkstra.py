from heapq import heappop, heappush

inf = float("inf")


# ed=隣接リスト[(next, weight)], 初期ノード
def dijkstra(ed, st):
    # 初期化
    n = len(ed)
    distance = [inf] * n
    distance[st] = 0
    heap = [(0, st)]
    # ダイクストラ
    while heap:
        dis, v = heappop(heap)
        if distance[v] < dis:
            continue
        for next, weight in ed[v]:
            new_distance = distance[v] + weight
            if new_distance < distance[next]:
                distance[next] = new_distance
                heappush(heap, (new_distance, next))
    return distance
