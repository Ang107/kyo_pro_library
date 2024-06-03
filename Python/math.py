# n以下の素数のリストを取得
def get_Sosuu(n):
    A = list(range(2, n + 1))
    p = list()
    while A[0] ** 2 <= n:
        tmp = A[0]
        p.append(tmp)
        A = [e for e in A if e % tmp != 0]
    return p + A


def get_primes(n):
    # n以下のすべての数について素数かどうかを記録する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = False  # 0は素数ではない
    is_prime[1] = False  # 1は素数ではない
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            # iの倍数を素数ではないとマーク
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    return primes


# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 素因数分解
# 戻り値は(素因数、指数)のタプル)
def factorization(n):
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
