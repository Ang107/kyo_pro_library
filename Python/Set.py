from collections import defaultdict


# 集合と各要素の個数を同時に管理するクラス
class Set:
    def __init__(self):
        self.s = set()
        self.dd = defaultdict(int)

    # 要素の追加(setと同じ感覚で使える)
    def add(self, x):
        self.s.add(x)
        self.dd[x] += 1

    # 要素の削除(setと同じ感覚で使える)
    def remove(self, x):
        self.dd[x] -= 1
        if self.dd[x] == 0:
            self.s.discard(x)

    def get_dd(self):
        return self.dd

    def get_s(self):
        return self.s

    def __len__(self):
        return len(self.s)

    # 指定した要素の個数の取得
    def __getitem__(self, key):
        return self.dd[key]

    # 指定した要素の個数の設定
    def __setitem__(self, key, val):
        self.dd[key] = val
        if self.dd[key] == 0:
            self.s.discard(key)

    def __bool__(self):
        return len(self.s) >= 1
