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
    # print('---------------------------')
    tmp = set(i for i in range(1, n + 1))
    # print(j)
    # print(tmp)
    k = list(tmp - set(j))
    work_com_morn = list(permutations(j,2))
    work_com_night = list(permutations(k,2))
    # print(work_com_morn)
    # print(work_com_night)
    morn_sum = 0
    night_sum = 0
    for x,y in work_com_morn:
        morn_sum += lst[y-1][x-1]
    for x,y in work_com_night:
        night_sum += lst[y-1][x-1]
    # print('m_sum', morn_sum)
    # print('n_sum', night_sum)
    result.append(abs(morn_sum - night_sum))


print(min(result))