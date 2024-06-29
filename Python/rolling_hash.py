import random


class RollingHash:
    def __init__(self, s: str):
        self.s = s
        self.MOD = 2**61 - 1
        self.B = random.randrange(100, 200)
        self.pow_B_mod = [1]
        for _ in range(len(s)):
            self.pow_B_mod.append(self.pow_B_mod[-1] * self.B % self.MOD)

    def make_hash_l(self) -> None:
        """左から見た文字列のrolling hashを計算。"""
        self.hash_l = [0]
        for i in self.s:
            self.hash_l.append((self.hash_l[-1] * self.B + ord(i)) % self.MOD)

    def make_hash_r(self) -> None:
        """右から見た文字列のrolling hashを計算。"""
        self.hash_r = [0]
        for i in self.s[::-1]:
            self.hash_r.append((self.hash_r[-1] * self.B + ord(i)) % self.MOD)
        self.hash_r = self.hash_r[::-1]

    def get_hash_l(self, l: int, r: int) -> int:
        """左から見た文字列のl番目からr番目までの文字列のハッシュの取得(0index)"""
        return (
            self.hash_l[r + 1] - self.pow_B_mod[r - l + 1] * self.hash_l[l]
        ) % self.MOD

    def get_hash_r(self, l: int, r: int) -> int:
        """右から見た文字列のl番目からr番目までの文字列のハッシュの取得(0index)"""
        return (
            self.hash_r[l] - self.pow_B_mod[r - l + 1] * self.hash_r[r + 1]
        ) % self.MOD
