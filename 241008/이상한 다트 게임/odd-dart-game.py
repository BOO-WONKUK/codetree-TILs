n,m,q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
lst_command = [list(map(int, input().split())) for _ in range(q)]

def rotate(x,d,k):
    for i in range(1,n+1):
        if i % x == 0:
            dx = 0
            if d == 0:
                dx = 1
            else:
                dx = -1

            lst_tmp = lst[i-1][:]
            for j in range(m):
                idx = (j + dx * k) % m
                lst_tmp[idx] = lst[i-1][j]
            lst[i-1] = lst_tmp[:]

        # for e in lst:
        #     print(*e)
        # print('-------------')



def check():
    lst_sub = [[0]* m  for _ in range(n)]
    dx,dy = [0,1],[1,0]
    for i in range(m):
        for j in range(n):
            for k in range(2):
                if k == 0 and j == n-1:
                    continue
                nx = (i + dx[k]) % m
                ny = (j + dy[k]) % m
                if lst[j][i] == lst[ny][nx] :
                    if lst_sub[j][i] == 0:
                        lst_sub[j][i] = 1
                    if lst_sub[ny][nx] == 0:
                        lst_sub[ny][nx] = 1

    del_cnt = 0
    cnt = 0
    sum_ = 0
    for i in range(m):
        for j in range(n):
            if lst_sub[j][i] == 1:
                del_cnt += 1
                lst[j][i] = -1
            else:
                cnt += 1
                sum_ += lst[j][i]
    # for e in lst:
    #     print(*e)
    # print('-------------')
    if cnt == 0:
        return 0,0,0                # 0 판에 숫자X -> 정규화 X
    elif del_cnt == 0:
        return cnt,sum_,1           # 1 지워지는 숫자 X -> 전체수 평균
    else:
        return cnt,sum_,2           # 2 지워지는 숫자 O -> 남은 수 평균



for z,x,c in lst_command:
    # for e in lst:
    #     print(*e)
    # print('-------------')
    rotate(z,x,c)
    # for e in lst:
    #     print(*e)
    # print('rotate-------------')
    cnt,sum_,ck_num = check()
    # for e in lst:
    #     print(*e)
    # print('check-------------')
    # print(cnt, sum_,ck_num)
    if ck_num == 0 or ck_num == 2:
        pass
    else:
        avg = sum_ // cnt
        for i in range(m):
            for j in range(n):
                if lst[j][i] != -1:
                    if lst[j][i] > avg:
                        lst[j][i] -= 1
                    elif lst[j][i] < avg:
                        lst[j][i] += 1
    # for e in lst:
    #     print(*e)
    # print('check-------------')

ans = 0
for i in range(m):
    for j in range(n):
        if lst[j][i] != -1:
            ans += lst[j][i]

print(ans)