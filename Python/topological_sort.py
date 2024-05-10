from collections import deque, defaultdict


def topological_sort(n: int, output_edge: defaultdict, input_edge: defaultdict):
    ans = []
    for i in range(1, n+1):
        if not input_edge[i]:
            ans.append(i)
    deq = deque(ans)
    while deq:
        x = deq.popleft()
        for e in output_edge[x]:
            input_edge[e].discard(x)
            if input_edge[e] == 0:
                deq.append(e)
                ans.append(e)
    if len(ans) == n:
        return ans
    return False
