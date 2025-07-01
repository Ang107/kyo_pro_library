import typing


class BIT:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, v: typing.Union[int, typing.List[typing.Any]]) -> None:
        if isinstance(v, int):
            self._n = v
            self.data = [0] * self._n
        else:
            self._n = len(v)
            self.data = [0] * self._n
            for i, x in enumerate(v):
                self.add(i, x)

    def __str__(self) -> str:
        return f"BIT: {[self.get(i) for i in range(self._n)]}"

    def __iter__(self) -> typing.Iterator[typing.Any]:
        return iter(self.get(i) for i in range(self._n))

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n
        return self.sum(p, p + 1)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n
        self.add(p, x - self.get(p))

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s
