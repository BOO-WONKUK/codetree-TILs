n,m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
result = []

def shape1(x,y):
    if 0<=x<=m-4 and 0<=y<=n-1:
        result.append(lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y][x+3])
    if 0<=x<=m-1 and 0<=y<=n-4:
        result.append(lst[y][x] + lst[y + 1][x] + lst[y + 2][x] + lst[y + 3][x])
def shape2(x,y):
    if 0<=x<=m-2 and 0<=y<=n-2:
        result.append(lst[y][x] + lst[y+1][x] + lst[y+1][x + 1] + lst[y][x+1])
def shape3(x,y):
    if 0<=x<=m-2 and 0<=y<=n-3:
        result.append(lst[y][x] + lst[y+1][x] + lst[y+2][x] + lst[y+2][x+1])
        result.append(lst[y][x+1] + lst[y + 1][x+1] + lst[y + 2][x+1] + lst[y + 2][x])
        result.append(lst[y][x] + lst[y][x + 1] + lst[y+1][x + 1] + lst[y + 2][x + 1])
        result.append(lst[y][x] + lst[y][x + 1] + lst[y + 1][x] + lst[y + 2][x])
    if 0<=x<=m-3 and 0<=y<=n-2:
        result.append(lst[y][x] + lst[y][x+1] + lst[y][x+2] + lst[y+1][x])
        result.append(lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y + 1][x+2])
        result.append(lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 1][x + 2] + lst[y + 1][x + 2])
        result.append(lst[y][x] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 1][x + 2])
def shape4(x,y):
    if 0<=x<=m-2 and 0<=y<=n-3:
        result.append(lst[y][x] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 2][x + 1])
        result.append(lst[y][x + 1] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 2][x])
    if 0<=x<=m-3 and 0<=y<=n-2:
        result.append(lst[y + 1][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y][x + 2])
        result.append(lst[y][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y + 1][x + 2])
def shape5(x,y):
    if 0<=x<=m-2 and 0<=y<=n-3:
        result.append(lst[y][x] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 2][x])
        result.append(lst[y][x + 1] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 2][x + 1])
    if 0<=x<=m-3 and 0<=y<=n-2:
        result.append(lst[y][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y][x + 2])
        result.append(lst[y][x + 1] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 1][x + 2])

for i in range(n):
    for j in range(m):
        shape1(j,i)
        shape2(j, i)
        shape3(j, i)
        shape4(j, i)
        shape5(j, i)

print(max(result))