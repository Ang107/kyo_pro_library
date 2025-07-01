def swag(l, k, mode="min"):
    from collections import deque

    """
    lの中から連続してk個選ぶ時、左端が 0 ~ i-k の時それぞれの最大値、最小値を取得。
    n - k + 1個のリストを返す。O(N)
    """
    deq = deque()
    result = []
    if mode == "min":
        for i, a in enumerate(l):
            while deq and l[deq[-1]] >= a:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                result.append(l[deq[0]])
    elif mode == "max":
        for i, a in enumerate(l):
            while deq and l[deq[-1]] <= a:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                result.append(l[deq[0]])
    return result
