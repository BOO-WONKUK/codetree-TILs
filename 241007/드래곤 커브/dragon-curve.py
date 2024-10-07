n = int(input())
lst_command = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0,-1,0,1], [1,0,-1,0]  # 우 상 좌 하
result = [[0 for _ in range(101)] for _ in range(101)]

def in_range(x,y):
    if 0<=x<=100 and 0<=y<=100:
        return True
    return False

def check_box():
    ans = 0
    for i in range(100):
        for j in range(100):
            if result[j][i] == 1 and result[j+1][i] == 1 and result[j][i+1] == 1 and result[j+1][i+1] == 1:
                ans += 1
    return ans

def save_result(x,y,d,g):
    history = []
    result[x][y] = 1
    for k in range(g+1):
        tmp = -1
        if k == 0:
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx,ny):
                result[nx][ny] = 1
                x, y = nx, ny
                history.append(d)
            else:
                break
        else:
            sub = reversed(history)
            for i in sub:
                i = (i+1) % 4
                nx = x + dx[i]
                ny = y + dy[i]
                if in_range(nx, ny):
                    result[nx][ny] = 1
                    x, y = nx, ny
                    history.append(i)
                else:
                    tmp = 1
                    break

        if tmp == 1:
            break


for x,y,d,g in lst_command:
    save_result(x,y,d,g)
print(check_box())