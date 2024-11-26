from typing import Generic, Iterable, Iterator, List, TypeVar, Callable

T = TypeVar("T")


class MyDeque(Generic[T]):
    """
    Double-ended queue with O(1) index access.
    """

    def __init__(self, v: Iterable[T] = (), maxlen: int = 1 << 60):
        """
        Initialize the deque with an optional iterable and maximum length.
        Time complexity: O(n), where n is the size of the input iterable.
        """
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
        """
        Iterate over the elements of the deque.
        Time complexity: O(n).
        """
        for i in reversed(range(self._l_delled, len(self._l))):
            yield self._l[i]
        for i in range(self._r_delled, len(self._r)):
            yield self._r[i]

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate over the deque in reverse order.
        Time complexity: O(n).
        """
        for i in reversed(range(self._r_delled, len(self._r))):
            yield self._r[i]
        for i in range(self._l_delled, len(self._l)):
            yield self._l[i]

    def __eq__(self, other) -> bool:
        """
        Check if this deque is equal to another iterable.
        Time complexity: O(n).
        """
        return list(self) == list(other)

    def __len__(self) -> int:
        """
        Return the number of elements in the deque.
        Time complexity: O(1).
        """
        return self._size

    def __str__(self) -> str:
        """
        Return a string representation of the deque.
        Time complexity: O(n).
        """
        return f"MyDeque: {list(self)}"

    def __contains__(self, x: T) -> bool:
        """
        Check if the deque contains the specified element.
        Time complexity: O(n).
        """
        return x in self._l[self._l_delled :] or x in self._r[self._r_delled :]

    def __getitem__(self, i) -> List[T] | T:
        """
        Access an element or a slice of the deque.
        Time complexity: O(1) for single access, O(k) for slicing.
        """
        if isinstance(i, slice):
            start, stop, step = i.indices(self._size)
            return [self[idx] for idx in range(start, stop, step)]
        else:
            assert 0 <= i < self._size or -self._size <= i < 0
            if i < 0:
                i += self._size
            if i < len(self._l) - self._l_delled:
                return self._l[-i - 1]
            else:
                return self._r[self._r_delled + i - (len(self._l) - self._l_delled)]

    def __setitem__(self, i: int, x: T) -> None:
        """
        Set the value at the specified index.
        Time complexity: O(1).
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l[-i - 1] = x
        else:
            self._r[self._r_delled + i - (len(self._l) - self._l_delled)] = x

    def __delitem__(self, i: int) -> None:
        """
        Delete the element at the specified index.
        Time complexity: O(n).
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        self.pop(i)

    def reverse(self) -> None:
        """
        Reverse the order of the deque in O(1).
        """
        self._l, self._r = self._r, self._l
        self._l_delled, self._r_delled = self._r_delled, self._l_delled

    def count(self, x: T) -> int:
        """
        Count the occurrences of the specified element.
        Time complexity: O(n).
        """
        return self._l[self._l_delled :].count(x) + self._r[self._r_delled :].count(x)

    def copy(self):
        """
        Create a shallow copy of the deque.
        Time complexity: O(n).
        """
        return MyDeque(list(self), maxlen=self.maxlen)

    def sort(self, *, key: Callable[[T], object] = None, reverse: bool = False) -> None:
        """
        Sort the deque in-place.
        Time complexity: O(n log n).
        """
        sorted_list = sorted(self, key=key, reverse=reverse)
        self._l = []
        self._r = sorted_list
        self._l_delled = 0
        self._r_delled = 0

    def index(self, x: T, start: int = 0, stop=None) -> int:
        """
        Find the first occurrence of the element in the range [start, stop).
        Time complexity: O(n).
        """
        if stop == None:
            stop = self._size
        if start < 0:
            start += self._size
        if stop < 0:
            stop += self._size
        start = max(0, start)
        stop = min(self._size, stop)

        for i in range(start, stop):
            if self[i] == x:
                return i
        raise ValueError(f"{x} is not in MyDeque")

    def append(self, x: T) -> None:
        """
        Add an element to the right end of the deque.
        Time complexity: O(1).
        """
        self._size += 1
        self._r.append(x)
        if self._size > self.maxlen:
            self.popleft()

    def clear(self) -> None:
        """
        Remove all elements from the deque.
        Time complexity: O(1).
        """
        self._l.clear()
        self._r.clear()
        self._l_delled = 0
        self._r_delled = 0
        self._size = 0

    def pop(self, i=-1) -> T:
        """
        Remove and return the element at the specified index.
        Time complexity: O(1) for ends, O(n) for middle.
        """
        assert 0 <= i <= self._size or -self._size <= i <= -1
        assert self._size > 0
        if i < 0:
            i += self._size
        self._size -= 1

        if i == self._size:
            if len(self._r) - self._r_delled > 0:
                return self._r.pop()
            else:
                self._l_delled += 1
                return self._l[self._l_delled - 1]
        else:
            if i < len(self._l) - self._l_delled:
                return self._l.pop(self._size - i - 1)
            else:
                return self._r.pop(self._r_delled + i - (len(self._l) - self._l_delled))

    def appendleft(self, x: T) -> None:
        """
        Add an element to the left end of the deque.
        Time complexity: O(1).
        """
        self._size += 1
        self._l.append(x)
        if self._size > self.maxlen:
            self.pop()

    def popleft(self) -> T:
        """
        Remove and return the leftmost element of the deque.
        Time complexity: O(1).
        """
        assert self._size > 0
        self._size -= 1
        if len(self._l) - self._l_delled > 0:
            return self._l.pop()
        else:
            self._r_delled += 1
            return self._r[self._r_delled - 1]

    def extend(self, v: Iterable[T]) -> None:
        """
        Extend the deque to the right with the elements from the iterable.
        Time complexity: O(k), where k is the length of the iterable.
        """
        for i in v:
            self.append(i)

    def extendleft(self, v: Iterable[T]) -> None:
        """
        Extend the deque to the left with the elements from the iterable.
        Time complexity: O(k), where k is the length of the iterable.
        """
        for i in v:
            self.appendleft(i)

    def insert(self, i: int, x: T) -> None:
        """
        Insert an element at the specified position.
        Time complexity: O(n).
        """
        assert self._size == self.maxlen
        assert 0 <= i <= self._size or -self._size <= i <= -1
        if i < 0:
            i += self._size
        if i < len(self._l) - self._l_delled:
            self._l.insert(len(self._l) - i, x)
        else:
            self._r.insert(self._r_delled + i - (len(self._l) - self._l_delled), x)
        self._size += 1

    def remove(self, x: T) -> None:
        """
        Remove the first occurrence of the specified element.
        Time complexity: O(n).
        """
        assert self._size > 0
        self.pop(self.index(x))

    def rotate(self, k: int = 1) -> None:
        """
        Rotate the deque n steps to the right. Negative values rotate to the left.
        Time complexity: O(k).
        """
        if self._size == 0:
            return
        k %= self._size
        if k > 0:
            for _ in range(k):
                self.appendleft(self.pop())
        else:
            for _ in range(-k):
                self.append(self.popleft())


class TwoStackDeque:
    __slots__ = ("front", "back")

    def __init__(self, iterable=None) -> None:
        init_arr = list(iterable) if iterable else []
        mid = len(init_arr) >> 1
        self.front = init_arr[:mid][::-1]
        self.back = init_arr[mid:]

    def _balance(self) -> None:
        source, target = (
            (self.front, self.back) if not self.back else (self.back, self.front)
        )
        mid = len(source) >> 1
        target.extend(source[: mid + 1][::-1])
        del source[: mid + 1]

    def append(self, item) -> None:
        self.back.append(item)

    def appendleft(self, item) -> None:
        self.front.append(item)

    def pop(self):
        if not self:
            raise IndexError("pop from empty deque")
        if not self.back:
            self._balance()
        return self.back.pop()

    def popleft(self):
        if not self:
            raise IndexError("popleft from empty deque")
        if not self.front:
            self._balance()
        return self.front.pop()

    def __getitem__(self, i: int):
        l = len(self)
        if i < -l or l <= i:
            raise IndexError("deque index out of range")
        i = i if i >= 0 else i + l
        if i < len(self.front):
            return self.front[~i]
        else:
            return self.back[i - len(self.front)]

    def __len__(self) -> int:
        return len(self.front) + len(self.back)


# ごりちゃんさんのDeque
class RingBufferDeque:
    def __init__(self, src_arr=[], max_size=300000):
        self.N = max(max_size, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l:
            raise IndexError("index out of range: " + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1 : self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full():
            self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N

    def appendleft(self, x):
        if self.is_full():
            self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() when buffer is empty")
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret

    def popleft(self):
        if self.is_empty():
            raise IndexError("popleft() when buffer is empty")
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return "Deque({0})".format(str(list(self)))


import time
from collections import deque
import random
import matplotlib.pyplot as plt
import numpy as np
import statistics
import matplotlib

matplotlib.use("Agg")  # GUIを使わない描画バックエンドを設定


# 特定操作の時間計測
def test_operation(deque_obj, operation, n):
    start_time = time.perf_counter()
    for _ in range(n):
        if operation == "append":
            deque_obj.append(random.randint(-100, 100))
        elif operation == "appendleft":
            deque_obj.appendleft(random.randint(-100, 100))
        elif operation == "pop":
            if len(deque_obj) > 0:
                deque_obj.pop()
        elif operation == "popleft":
            if len(deque_obj) > 0:
                deque_obj.popleft()
        elif operation == "random_access":
            if len(deque_obj) > 0:
                index = random.randrange(len(deque_obj))
                _ = deque_obj[index]
    return time.perf_counter() - start_time


def run_tests(deque_class, size, operations, repetitions, num_trials=5):
    results = {}
    for op in operations:
        op_times = []
        for _ in range(num_trials):
            deque_obj = deque_class(list(range(size)))
            op_times.append(test_operation(deque_obj, op, repetitions))
        results[op] = {
            "mean": statistics.mean(op_times),
            "stdev": statistics.stdev(op_times) if len(op_times) > 1 else 0,
        }
    return results


# テスト結果の描画関数
def plot_results(sizes, std_results, rb_results, ts_results, my_results, operations):
    fig, axs = plt.subplots(
        len(operations), 1, figsize=(10, 4 * len(operations)), sharex=True
    )
    fig.suptitle("Deque Performance Comparison", y=1.02)

    x = np.arange(len(sizes))
    width = 0.25

    for i, op in enumerate(operations):
        std_times = [std_results[size][op]["mean"] for size in sizes]
        rb_times = [rb_results[size][op]["mean"] for size in sizes]
        ts_times = [ts_results[size][op]["mean"] for size in sizes]
        my_times = [my_results[size][op]["mean"] for size in sizes]

        std_err = [std_results[size][op]["stdev"] for size in sizes]
        rb_err = [rb_results[size][op]["stdev"] for size in sizes]
        ts_err = [ts_results[size][op]["stdev"] for size in sizes]
        my_err = [my_results[size][op]["stdev"] for size in sizes]

        axs[i].bar(
            x - width,
            std_times,
            width,
            yerr=std_err,
            label="Std Deque",
            color="blue",
            capsize=5,
        )
        axs[i].bar(
            x,
            rb_times,
            width,
            yerr=rb_err,
            label="Ring buffer Deque",
            color="green",
            capsize=5,
        )
        axs[i].bar(
            x + width,
            ts_times,
            width,
            yerr=ts_err,
            label="Two Stack Deque",
            color="red",
            capsize=5,
        )
        axs[i].bar(
            x + 2 * width,
            my_times,
            width,
            yerr=ts_err,
            label="MyDeque",
            color="Yellow",
            capsize=5,
        )

        axs[i].set_ylabel("Time (s)")
        axs[i].set_title(f"{op} Operation")
        axs[i].set_xticks(x)
        axs[i].set_xticklabels(sizes)
        axs[i].legend(loc="upper left")

        # random_accessの場合のみ対数スケールを使用
        if op == "random_access":
            axs[i].set_yscale("log")
        else:
            axs[i].set_yscale("linear")

    plt.xlabel("Number of Elements")
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.savefig("output_plot.png")


# テスト実行
sizes = [1000, 10000, 100000, 1000000]
operations = ["append", "appendleft", "pop", "popleft", "random_access"]
repetitions = 10000
num_trials = 100  # 試行回数

std_results = {}
rb_results = {}
ts_results = {}
my_results = {}

for size in sizes:
    print(f"Testing with {size} elements:")
    std_results[size] = run_tests(deque, size, operations, repetitions, num_trials)
    rb_results[size] = run_tests(
        RingBufferDeque, size, operations, repetitions, num_trials
    )
    ts_results[size] = run_tests(
        TwoStackDeque, size, operations, repetitions, num_trials
    )
    my_results[size] = run_tests(MyDeque, size, operations, repetitions, num_trials)
    # print("Standard deque results:", std_results[size])
    # print("Ring Buffer deque results:", rb_results[size])
    # print("Two Stack deque results:", ts_results[size])
    # print()

# 結果を描画
plot_results(sizes, std_results, rb_results, ts_results, my_results, operations)
