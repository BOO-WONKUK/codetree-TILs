n,m,t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
top_to = (-1, -1)
bot_to = (-1, -1)
dx,dy = [1,0,-1,0],[0,-1,0,1] # 우 상 좌 하
for i in range(m):
    for j in range(n):
        if lst[j][i] == -1:
            if top_to == (-1, -1):
                top_to = (i, j)
            else:
                bot_to = (i, j)
                
def in_range(x,y):
    if 0<=x<=m-1 and 0<=y<=n-1:
        return True
    return False

def simulate():
    lst_sub = [[0]*m for _ in range(n)]
    lst_plus = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if lst[j][i] >= 5:
                sum_ = 0
                tmp = lst[j][i] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (nx,ny) == bot_to or (nx,ny) == top_to:
                        continue

                    if in_range(nx,ny) :
                        lst_plus[ny][nx] += tmp
                        sum_ += tmp
                lst_sub[j][i] -= sum_



    for i in range(m):  # 확산 양만큼 기존 감소
        for j in range(n):
            lst[j][i] += (lst_sub[j][i] + lst_plus[j][i])

    nx, ny = top_to
    to_dust1 = 0
    for i in range(4):
        while True:
            ax = nx + dx[i]
            ay = ny + dy[i]
            if i == 3 and lst[ay][ax] == -1:
                break
            if not in_range(ax, ay):
                break

            tmp1 = lst[ay][ax]
            lst[ay][ax] = to_dust1
            to_dust1 = tmp1
            nx,ny = ax,ay

    nx, ny = bot_to
    to_dust2 = 0
    for i in range(4,0,-1):
        while True:
            i %= 4
            ax = nx + dx[i]
            ay = ny + dy[i]
            if i == 1 and lst[ay][ax] == -1:
                break
            if not in_range(ax, ay):
                break
            tmp2 = lst[ay][ax]
            lst[ay][ax] = to_dust2
            to_dust2 = tmp2
            nx,ny = ax,ay

for _ in range(t):
    simulate()

ans = 0

for i in range(m):
    for j in range(n):
        if lst[j][i] != -1:
            ans += lst[j][i]

print(ans)