n,m,k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def rotation():
    rotate_box = min(n,m) // 2

    for i in range(rotate_box):
        n_max = n - i - 1
        m_max = m - i - 1

        tmp_left_top = lst[i][i]

        for x in range(i,m_max): # 상단
            lst[i][x] = lst[i][x+1]
        for x in range(i,n_max): # 좌단
            lst[x][m_max] = lst[x+1][m_max]
        for x in range(m_max,i,-1): # 하단
            lst[m_max][x] = lst[m_max][x-1]
        for x in range(n_max,i, -1):
            lst[x][i] = lst[x-1][i]
        lst[i+1][i] = tmp_left_top
for _ in range(k):
    rotation()

for i in lst:
    print(*i)