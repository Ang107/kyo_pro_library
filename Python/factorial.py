class Factorial:
    """
    階乗 / 逆階乗を必要になったぶんだけ動的に拡張するクラス。
    逆元は『一括逆元法』で計算するので高速。
    comb(n, r) は nCr を O(1) で返す。
    """

    def __init__(self, n: int = 0, MOD: int = 998244353):
        assert n < MOD, "MOD 以上の階乗は逆元が取れません"
        self.MOD = MOD
        # 0! から n! まで作る（まだ逆元は作らない）
        self._factorials = [1]
        for k in range(1, n + 1):
            self._factorials.append(self._factorials[-1] * k % MOD)

        # 逆階乗テーブル（先に正しい長さだけ確保）
        self._inv_factorials = [1] * (n + 1)
        if n:
            # 一括逆元法：まず n! の逆元を 1 回だけ pow で取る
            self._inv_factorials[n] = pow(self._factorials[n], -1, MOD)
            # 後ろから流し込む
            for k in range(n, 0, -1):
                self._inv_factorials[k - 1] = self._inv_factorials[k] * k % MOD

    # ---------- 内部ユーティリティ ---------- #
    def _extend(self, n: int) -> None:
        """テーブルを n まで拡張。既に長ければ何もしない。"""
        if n < len(self._factorials):
            return
        assert n < self.MOD, "MOD 以上の階乗は逆元が取れません"

        old_len = len(self._factorials)  # 旧サイズ (＝最大 index + 1)

        # 1. 階乗を前方向に追加
        for k in range(old_len, n + 1):
            self._factorials.append(self._factorials[-1] * k % self.MOD)

        # 2. 逆階乗テーブルを後ろから畳み込む
        self._inv_factorials.extend([0] * (n + 1 - old_len))
        self._inv_factorials[n] = pow(self._factorials[n], -1, self.MOD)
        for k in range(n, old_len, -1):  # 新規に増えた部分だけ
            self._inv_factorials[k - 1] = self._inv_factorials[k] * k % self.MOD

    # ---------- 公開 API ---------- #
    def comb(self, n: int, r: int) -> int:
        """nCr を返す（範囲外は 0）"""
        assert r >= 0 and r <= n and n < self.MOD
        self._extend(n)
        return (
            self._factorials[n]
            * self._inv_factorials[r]
            % self.MOD
            * self._inv_factorials[n - r]
            % self.MOD
        )

    def fac(self, n: int) -> int:
        assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._factorials[n]

    def inv_fac(self, n: int) -> int:
        assert n >= 0 and n < self.MOD
        self._extend(n)
        return self._inv_factorials[n]
