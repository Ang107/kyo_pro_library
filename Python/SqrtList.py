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


def test_sqrtlist():
    import random

    # 基本動作のテスト
    print("Testing basic operations...")

    sqrt_list = SqrtList[int]()
    standard_list = []

    # Append テスト
    for i in range(10):
        sqrt_list.append(i)
        standard_list.append(i)
        assert list(sqrt_list) == standard_list, f"Failed append test at {i}"

    # AppendLeft テスト
    for i in range(10, 15):
        sqrt_list.appendleft(i)
        standard_list.insert(0, i)
        assert list(sqrt_list) == standard_list, f"Failed appendleft test at {i}"

    # Insert テスト
    for i in range(5):
        pos = random.randint(0, len(standard_list))
        sqrt_list.insert(pos, 100 + i)
        standard_list.insert(pos, 100 + i)
        assert (
            list(sqrt_list) == standard_list
        ), f"Failed insert test at {i}, position {pos}"

    # GetItem テスト
    for i in range(len(standard_list)):
        assert sqrt_list[i] == standard_list[i], f"Failed getitem test at {i}"

    # SetItem テスト
    for i in range(len(standard_list)):
        sqrt_list[i] = -standard_list[i]
        standard_list[i] = -standard_list[i]
        assert list(sqrt_list) == standard_list, f"Failed setitem test at {i}"

    # Pop テスト
    for _ in range(5):
        pos = random.randint(0, len(standard_list) - 1)
        sqrt_list.pop(pos)
        standard_list.pop(pos)
        assert list(sqrt_list) == standard_list, f"Failed pop test at position {pos}"

    # PopLeft テスト
    for _ in range(5):
        sqrt_list.popleft()
        standard_list.pop(0)
        assert list(sqrt_list) == standard_list, "Failed popleft test"

    # Count テスト
    sqrt_list.append(42)
    standard_list.append(42)
    assert sqrt_list.count(42) == standard_list.count(42), "Failed count test"

    # Contains テスト
    assert (42 in sqrt_list) == (42 in standard_list), "Failed contains test"

    print("All basic operation tests passed!")

    # 大規模データの性能テスト
    print("Testing large data operations...")
    large_list = list(range(1000))
    sqrt_large = SqrtList(large_list)
    assert list(sqrt_large) == large_list, "Failed large data initialization"

    # ランダム挿入/削除テスト
    for _ in range(100):
        if random.choice([True, False]):
            # Insert
            pos = random.randint(0, len(large_list))
            value = random.randint(0, 1000)
            sqrt_large.insert(pos, value)
            large_list.insert(pos, value)
        else:
            # Pop
            if len(large_list) > 0:
                pos = random.randint(0, len(large_list) - 1)
                sqrt_large.pop(pos)
                large_list.pop(pos)
        assert list(sqrt_large) == large_list, "Failed random operation test"

    print("All large data operation tests passed!")


# 実行
test_sqrtlist()
