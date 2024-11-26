from collections import deque, defaultdict


def topological_sort(n: int, output_edge, input_edge_num):
    ans = []
    for i in range(n):
        if input_edge_num[i] == 0:
            ans.append(i)
    deq = deque(ans)
    while deq:
        x = deq.popleft()
        for next in output_edge[x]:
            input_edge_num[next] -= 1
            if input_edge_num[next] == 0:
                deq.append(next)
                ans.append(next)
    if len(ans) == n:
        return ans
    return False
