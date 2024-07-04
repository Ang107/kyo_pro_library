import random


class RollingHash:
    def __init__(self, s: str, base: int = None, mod: int = 2**61 - 1):
        self.s = s
        self.MOD = mod
        self.base = base if base is not None else random.randrange(100, 200)
        self.pow_base_mod = [1]
        for _ in range(len(s)):
            self.pow_base_mod.append(self.pow_base_mod[-1] * self.base % self.MOD)
        self.make_hash_l()
        self.make_hash_r()

    def make_hash_l(self) -> None:
        """左から見た文字列のrolling hashを計算。"""
        self.hash_l = [0]
        for i in self.s:
            self.hash_l.append((self.hash_l[-1] * self.base + ord(i)) % self.MOD)

    def make_hash_r(self) -> None:
        """右から見た文字列のrolling hashを計算。"""
        self.hash_r = [0]
        for i in self.s[::-1]:
            self.hash_r.append((self.hash_r[-1] * self.base + ord(i)) % self.MOD)
        self.hash_r = self.hash_r[::-1]

    def get_hash_l(self, l: int, r: int) -> int:
        """左から見た文字列[l, r)のハッシュの取得(0_index)"""
        if l < 0 or r > len(self.s) or l > r:
            raise ValueError(
                f"get {l=}, {r=}, but expected 0 <= l <= r <= {len(self.s)}"
            )
        return (self.hash_l[r] - self.pow_base_mod[r - l] * self.hash_l[l]) % self.MOD

    def get_hash_r(self, l: int, r: int) -> int:
        """右から見た文字列[l, r)のハッシュの取得(0_index)"""
        if l < 0 or r > len(self.s) or l > r:
            raise ValueError(
                f"get {l=}, {r=}, but expected 0 <= l <= r <= {len(self.s)}"
            )
        return (self.hash_r[l] - self.pow_base_mod[r - l] * self.hash_r[r]) % self.MOD


# 使用例
# rh = RollingHash("example")
# print(rh.get_hash_l(4, 3))  # "exa"のハッシュを取得
# print(rh.get_hash_r(0, 3))  # "exa"の右から見たハッシュを取得
