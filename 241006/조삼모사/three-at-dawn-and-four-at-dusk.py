from itertools import  combinations,permutations

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
sub = [i for i in range(1,n+1)]
com = list(combinations(sub,n//2))
lst_com = []
result = []

for j in com:
    tmp = set(i for i in range(1,n+1))
    k = tmp - set(j)
    if list(k) not in lst_com and list(j) not in lst_com:
        lst_com.append(list(j))

for j in lst_com:
    tmp = set(i for i in range(1, n + 1))
    k = list(tmp - set(j))

    work_com_morn = list(combinations(j,2))
    work_com_night = list(combinations(k,2))

    morn_sum = 0
    night_sum = 0

    for x,y in work_com_morn:
        morn_sum += lst[y-1][x-1]
        morn_sum += lst[x - 1][y - 1]
    for x,y in work_com_night:
        night_sum += lst[y-1][x-1]
        night_sum += lst[x - 1][y - 1]

    result.append(abs(morn_sum - night_sum))


print(min(result))