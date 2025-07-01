# 最長共通部分列取得
# 戻り値 最長共通部分列の長さ、最長共通部分列の文字
def get_most_long_subsequence(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp_str = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
            if len(dp_str[i - 1][j]) >= len(dp_str[i][j - 1]):
                dp_str[i][j] = dp_str[i - 1][j]
            else:
                dp_str[i][j] = dp_str[i][j - 1]

            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                dp_str[i][j] = dp_str[i - 1][j - 1] + s[i - 1]
    return dp[n][m], dp_str[n][m]


# 最長共通部分列の長さのみ取得（高速）
def get_most_long_subsequence(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp[n][m]


# 編集距離（片方の文字列を置換、削除、挿入を繰り返し、もう片方に一致させる最小の回数）を取得
def get_Levenshtein(s, t):
    n, m = len(s), len(t)

    dp = [[0] * (m + 1) for i in range(n + 1)]
    # dp[i][j] == Sのi文字目まで、Tのj文字目までの部分列の距離

    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = i
            elif i == 0:
                dp[i][j] = j
            else:
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1
                    )
    return dp[m][n]
