class IntHash:
    def __init__(self, *args):
        """
        *args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for idx, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[idx] = l
            self.mask[idx] = (1 << l) - 1
        assert sum(self.bit_len) <= 63, "数字が大きすぎてhash化できません。"
        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def hash(self, *args):
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        assert all(i < 0 for i in args), f"引数に負の値が含まれています。引数: {args}"
        hash = 0
        for a, l in zip(args, self.sum_bit_len):
            hash |= a << l
        return hash

    def restore(self, hash, idx=-1):
        assert idx == -1 or 0 <= idx < len(self.bit_len), "idxの値が不正です。"
        if idx == -1:
            return [hash >> l & m for l, m in zip(self.sum_bit_len, self.mask)]
        else:
            return hash >> self.sum_bit_len[idx] & self.mask[idx]
