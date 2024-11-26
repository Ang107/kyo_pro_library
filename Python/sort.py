import typing
from collections import defaultdict, deque


class BIT:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


# AをBにするのに必要な転倒数を計算
# O(NlogN)
def get_inversion_number(A, B):
    to_idx = defaultdict(deque)
    for idx, a in enumerate(A):
        to_idx[a].append(idx)
    nB = []
    for i in B:
        nB.append(to_idx[i][0])
        to_idx[i].popleft()
    bit = BIT(len(nB))
    ans = 0
    for idx, i in enumerate(nB):
        ans += bit.sum(i + 1, len(nB))
        bit.add(i, 1)
    return ans
