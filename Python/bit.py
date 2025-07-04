def popcount(n: int):
    # 64bit以下の整数に対するpopcount
    # python3.10以降ならint.bit_count()でよい
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


class BitSet:
    """
    bitを用いたset
    非負整数の集合を管理できる
    挿入・削除・存在判定がO(1)
    要素の全列挙ができない
    ハックはされない
    """

    def __init__(self, max_num: int):
        assert max_num <= 10**9, "大きすぎます"
        self._max_num = max_num
        max_num += 1
        self._bit_length = -1
        self._blocks = -1
        self._bits = []
        self._n = 0
        # リストの要素数を求める
        for i in range(63, 1024, 64):
            if max_num // i <= 1000000:
                self._bit_length = i
                self._blocks = max_num // i + 1
                self._bits = [0] * self._blocks
                break

    def add(self, x: int) -> bool:
        """
        要素を追加する
        既にあった場合はFalse,新規で追加さ入れた場合はTrueを返す
        """
        assert x <= self._max_num
        block_idx, idx = x // self._bit_length, x % self._bit_length
        if self._bits[block_idx] >> idx & 1:
            return False
        else:
            self._bits[block_idx] |= 1 << idx
            self._n += 1
            return True

    def discard(self, x: int) -> bool:
        """
        要素を削除する
        存在した場合はTrue,存在しなかった場合はFalseを返す
        """
        assert x <= self._max_num
        block_idx, idx = x // self._bit_length, x % self._bit_length
        if self._bits[block_idx] >> idx & 1:
            self._bits[block_idx] &= ~(1 << idx)
            self._n -= 1
            return True
        else:
            return False

    def __contains__(self, x: int) -> bool:
        """
        存在判定
        """
        assert x <= self._max_num
        block_idx, idx = x // self._bit_length, x % self._bit_length
        return self._bits[block_idx] >> idx & 1

    def __len__(self) -> int:
        return self._n
