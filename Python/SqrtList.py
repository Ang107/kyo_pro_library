# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py を元に改造したものです。
import math
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar

T = TypeVar("T")


class SqrtList(Generic[T]):
    """
    任意位置へのランダムアクセス・挿入・削除がそこそこ高速(O(√N))なリスト
    """

    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = ()) -> None:
        a = list(a)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SqrtList" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def __contains__(self, x: T) -> bool:
        for a in self.a:
            if x in a:
                return True
        return False

    def count(self, x: T) -> int:
        ans = 0
        for a in self.a:
            ans += a.count(x)
        return ans

    def _position(self, i: int) -> Tuple[List[T], int, int]:
        if i < 0:
            i = -i - 1
            for b, a in enumerate(reversed(self.a)):
                if i >= len(a):
                    i -= len(a)
                else:
                    return a, len(self.a) - b - 1, len(a) - i - 1
            return self.a[0], 0, 0
        else:
            for b, a in enumerate(self.a):
                if i >= len(a):
                    i -= len(a)
                else:
                    return a, b, i
            return self.a[-1], len(self.a) - 1, len(self.a[-1])

    def append(self, x: T) -> None:
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self.a[-1], len(self.a) - 1, len(self.a[-1])
        a.append(x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def appendleft(self, x: T) -> None:
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self.a[0], 0, 0
        a.insert(0, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def insert(self, i: int, x: T) -> None:
        assert 0 <= i <= self.size + 1 or -self.size <= i <= -1, (i, self.size)
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self._position(i)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def __getitem__(self, i: int) -> T:
        assert 0 <= i <= self.size or -self.size <= i <= -1
        a, _, i = self._position(i)
        return a[i]

    def __setitem__(self, i: int, x: T) -> None:
        assert 0 <= i <= self.size or -self.size <= i <= -1
        a, _, i = self._position(i)
        a[i] = x

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def pop(self, i: int = -1) -> T:
        assert self.size != 0
        assert 0 <= i < self.size or -self.size <= i <= -1
        a, b, i = self._position(i)
        return self._pop(a, b, i)

    def popleft(self, i: int = 0) -> T:
        assert self.size != 0
        assert 0 <= i < self.size or -self.size <= i <= -1
        a, b, i = self._position(i)
        return self._pop(a, b, i)
