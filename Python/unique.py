# リストに含まれる要素の種類数を返す(O(NlogN))
# setよりも早い場合あり
def unique_cnt(a: list) -> int:
    if not a:
        return 0
    a = sorted(a)
    ans = 1
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            ans += 1
    return ans


def get_unique(a: list) -> list:
    a = sorted(a)
    ans = [a[0]]
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            ans.append(a[i])
    return ans
