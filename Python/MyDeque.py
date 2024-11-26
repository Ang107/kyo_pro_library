from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class MyDeque(Generic[T]):
    """
    インデックスアクセスがO(1)な両端キュー
    """

    def __init__(self, v: Iterable[T] = (), maxlen: int = 1 << 60):
        assert len(v) <= maxlen
        self.maxlen = maxlen
        self._size = len(v)
        self._l: List[T] = []
        self._r: List[T] = []
        for i, x in enumerate(v):
            if i < self._size >> 1:
                self._l.append(x)
            else:
                self._r.append(x)
        self._l.reverse()
        self._l_delled = 0
        self._r_delled = 0

    def __iter__(self) -> Iterator[T]:
        for i in reversed(range(self._l_delled, len(self._l))):
            yield self._l[i]
        for i in range(self._r_delled, len(self._r)):
            yield self._r[i]

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(range(self._r_delled, len(self._r))):
            yield self._r[i]
        for i in range(self._l_delled, len(self._l)):
            yield self._l[i]

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"MyDeque: {list(self)}"

    def __contains__(self, x: T) -> bool:
        return x in self._l[self._l_delled :] or x in self._r[self._r_delled :]

    def __getitem__(self, i: int) -> T:
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            return self._l[-i - 1]
        else:
            return self._r[self._r_delled + i - (len(self._l) - self._l_delled)]

    def __setitem__(self, i: int, x: T) -> None:
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l[-i - 1] = x
        else:
            self._r[self._r_delled + i - (len(self._l) - self._l_delled)] = x

    def count(self, x: T) -> int:
        return self._l[self._l_delled :].count(x) + self._r[self._r_delled :].count(x)

    def append(self, x: T) -> None:
        self._size += 1
        self._r.append(x)
        if self._size > self.maxlen:
            self.popleft()

    def pop(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._r) - self._r_delled > 0:
            return self._r.pop()
        else:
            self._l_delled += 1
            return self._l[self._l_delled - 1]

    def appendleft(self, x: T) -> None:
        self._size += 1
        self._l.append(x)
        if self._size > self.maxlen:
            self.pop()

    def popleft(self) -> T:
        assert self._size > 0
        self._size -= 1
        if len(self._l) - self._l_delled > 0:
            return self._l.pop()
        else:
            self._r_delled += 1
            return self._r[self._r_delled - 1]
