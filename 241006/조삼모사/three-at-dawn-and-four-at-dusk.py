from itertools import combinations

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
sub = [i for i in range(n)]  # 1-based index를 0-based로 바꿈

com = list(combinations(sub, n // 2))
result = []

for j in com:
    k = list(set(sub) - set(j))

    morn_sum = 0
    night_sum = 0

    # 아침 작업 강도 합계
    for x in range(n // 2):
        for y in range(x + 1, n // 2):
            morn_sum += lst[j[x]][j[y]]
            morn_sum += lst[j[y]][j[x]]

    # 저녁 작업 강도 합계
    for x in range(n // 2):
        for y in range(x + 1, n // 2):
            night_sum += lst[k[x]][k[y]]
            night_sum += lst[k[y]][k[x]]

    result.append(abs(morn_sum - night_sum))

print(min(result))