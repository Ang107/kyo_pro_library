def get_primes(n):
    """
    エラストテネスの篩
    O(NloglogN)でN以下の素数を列挙する
    """
    if n <= 1:
        return []
    # n以下のすべての数について素数かどうかを記録する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = False  # 0は素数ではない
    is_prime[1] = False  # 1は素数ではない
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return primes


def is_prime(n):
    """
    ミラー・ラビン素数判定法を用いた素数判定
    2 ^ 64 未満の整数で正確に判定可能
    重めのO(1)と思って良い
    """
    if n == 2:  # 2であれば素数なので終了
        return 1
    if n == 1 or n % 2 == 0:  # 1もしくは2より大きい偶数であれば素数でないので終了
        return 0

    m = n - 1
    lsb = m & -m  # LSB. m-1をビット列で表した時立っているビットのうち最も小さいもの
    s = (
        lsb.bit_length() - 1
    )  # 上述のs. LSB以上のビットの部分をdとし、2^s = LSBとすると上述のp-1 = 2^sdを満たす
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:  # a = n -> 任意の自然数kについてa^k ≡ 0(mod n)なので無視
            continue
        x = pow(a, d, n)  # x ≡ a^d(mod n)で初期化
        r = 0
        if x == 1:  # a^d ≡ 1(mod n)なので無視
            continue
        while x != m:  # r = 0からsまで順にx ≡ a^(2^rd) ≡ -1(mod n)を検証
            x = pow(x, 2, n)
            r += 1
            if (
                x == 1 or r == s
            ):  # x ≡ 1(mod n) -> x^2 ≡ 1(mod n)で-1になり得ないので合成数
                return 0
    return 1  # すべてのテストを通過したら素数であるとして終了


def make_divisors(n, primes=-1):
    """
    昇順に約数列挙
    O(√N)
    昇順に並んだ素数を引数に渡すことで定数倍高速化可能
    """
    if primes == -1:
        lower_divisors, upper_divisors = [], []
        for i in range(1, n):
            if i * i > n:
                break
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
        return lower_divisors + upper_divisors[::-1]
    else:
        assert n <= primes[-1] * primes[-1]
        lower_divisors, upper_divisors = [], []
        for i in primes:
            if i * i > n:
                break
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
        return lower_divisors + upper_divisors[::-1]


# 素因数分解
# 戻り値は(素因数、指数)のタプル)
def factorization(n):
    """
    素因数分解
    O(√N)
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# n進数->10進数
def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


# 10進数->n進数
def base_n(num_10, n, **kwargs):
    trans = kwargs.get("trans", list(map(str, range(n))))
    # print(trans)
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        str_n += trans[num_10 % n]
        num_10 //= n
    return str_n[::-1]


def extended_gcd(a, b):
    """拡張ユークリッドの互除法を用いて、ax + by = gcd(a, b) を満たす整数 x, y を求める"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def find_integer_solution(a, b, c):
    """ax + by = c を満たす整数 x, y を求める"""
    gcd, x0, y0 = extended_gcd(a, b)

    # c が gcd(a, b) で割り切れない場合、整数解は存在しない
    if c % gcd != 0:
        return False

    # ax0 + by0 = gcd(a, b) の倍数が解の一つなので、両辺を c / gcd(a, b) で割る
    factor = c // gcd
    x = x0 * factor
    y = y0 * factor

    return x, y
