class TupleHash:
    def __init__(self, *args):
        """
        *args: 各要素の取りうる値の最大値
        """
        self.bit_len = [-1] * len(args)
        self.mask = [-1] * len(args)
        for index, i in enumerate(args):
            l = len(bin(i)) - 2
            self.bit_len[index] = l
            self.mask[index] = (1 << l) - 1
        if sum(self.bit_len) > 63:
            from sys import stderr

            print("数字が大きすぎるため、低速になる可能性があります。", file=stderr)

        self.sum_bit_len = [0]
        for i in self.bit_len[1:][::-1]:
            self.sum_bit_len.append(self.sum_bit_len[-1] + i)
        self.sum_bit_len = self.sum_bit_len[::-1]

    def encode(self, *args):
        """
        タプルを整数にエンコード
        """
        assert len(self.bit_len) == len(args), "引数の数が一致しません。"
        assert all(0 <= i for i in args), f"引数に負の値が含まれています。引数: {args}"
        res = 0
        for a, l in zip(args, self.sum_bit_len):
            res |= a << l
        return res

    def deocde(self, res, index=None):
        """
        整数から元のタプルにデコード
        index: 特定の要素だけ取得する場合（省略時は全要素を取得）
        """
        assert index == None or 0 <= index < len(self.bit_len), "idxの値が不正です。"
        if index == None:
            return (res >> l & m for l, m in zip(self.sum_bit_len, self.mask))
        else:
            return res >> self.sum_bit_len[index] & self.mask[index]
