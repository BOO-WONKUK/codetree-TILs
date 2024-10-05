n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

t = [i[0] for i in lst]
p = [i[1] for i in lst]

dp = p[:]

for i in range(n):
    if t[i] + i > n:
        continue
    
    for j in range(i):
        if t[j] < i - j:
            if t[i] + i <= n:
                dp[i] = max(dp[i], dp[j] + p[i])

print(max(dp))