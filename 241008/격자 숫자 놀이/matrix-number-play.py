r,c,k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(3)]

def in_range(x,y):
    row = len(lst)
    col = len(lst[0])
    if 0<=x<=col and 0<=y<=row:
        return True
    return False

def simulate():
    global lst # 왜 써야하는가?
    row = len(lst)
    col = len(lst[0])

    if row >= col:
        sub_len = 0
        lst_plus = []
        for i in range(row):
            cnt = 0
            lst_count = [[i,0] for i in range(101)]
            for j in lst[i]:
                lst_count[j][1] += 1
            lst_tmp = []
            for a,b in lst_count:
                if b >= 1and a>=1:
                    cnt += 1
                    lst_tmp.append([a,b])
            lst_plus.append(lst_tmp)
            sub_len = max(cnt*2,sub_len)

        lst_sub = [[0] * sub_len for _ in range(row)]

        for i in range(len(lst_plus)):
            idx = 0
            for a,b in sorted(lst_plus[i], key= lambda x:(x[1],x[0])):
                lst_sub[i][idx] = a
                lst_sub[i][idx+1] = b
                idx+=2
        lst = lst_sub[0:100]



    else: # row < col
        sub_len = 0
        lst_plus = []
        for i in range(col):
            cnt = 0
            lst_count = [[i, 0] for i in range(101)]
            for k in range(row):
                lst_count[lst[k][i]][1] += 1
            lst_tmp = []
            for a, b in lst_count:
                if b >= 1 and a>=1:
                    cnt += 1
                    lst_tmp.append([a, b])
            # print('lst_tmp' , lst_tmp)
            lst_plus.append(lst_tmp)
            sub_len = max(cnt * 2, sub_len)

        lst_sub = [[0] * col for _ in range(sub_len)]

        for i in range(len(lst_plus)):
            idx = 0
            for a, b in sorted(lst_plus[i], key=lambda x: (x[1], x[0])):
                lst_sub[idx][i] = a
                lst_sub[idx + 1][i] = b
                idx += 2
        lst = lst_sub[0:100]
    # for i in lst:
    #     print(*i)
    # print('-------------')
time = 0
if in_range(c, r) and lst[r - 1][c - 1] == k:
    print(time)

else:
    while True:
        simulate()
        time += 1
        if in_range(c,r) and lst[r-1][c-1] == k:
            print(time)
            # for i in lst:
            #     print(*i)
            break
        if time >= 100:
            print(-1)
            break