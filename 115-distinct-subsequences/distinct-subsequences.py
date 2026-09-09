class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        a = [[0] * (n) for _ in range(m)]
        for i in range(m):
            a[i][0] = (a[i-1][0] if i > 0 else 0) + 1 * (s[i] == t[0])
        for j in range(1, n):
            for i in range(1,m):
                a[i][j] = a[i-1][j]
                if s[i] == t[j]:
                    a[i][j] += a[i-1][j-1]
        return a[m-1][n-1]