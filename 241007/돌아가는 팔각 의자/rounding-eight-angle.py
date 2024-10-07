lst_table = [list(map(int,list(input()))) for _ in range(4)]
n = int(input())
lst_command = [list(map(int, input().split())) for _ in range(n)]

def check(a,b): # a < b
    if lst_table[a - 1][2] != lst_table[b - 1][6]:
        return True
    else:
        return False

def rotate(k,d):
    sub = lst_table[k-1][:]
    if d == 1:
        for i in range(8):
            sub[i] = lst_table[k - 1][(i - 1) % 8]
        lst_table[k-1] = sub[:]  #[:] 와 없는것이 차이가 있나?
    elif d == -1:
        for i in range(8):
            sub[i] = lst_table[k - 1][(i + 1) % 8]
        lst_table[k-1] = sub[:]

for i,j in lst_command:
    if i == 1:
        if check(1,2):
            if check(2,3):
                if check(3,4):
                    rotate(4,-j)
                rotate(3,j)
            rotate(2, -j)
        rotate(1, j)

    elif i == 2:
        if check(1,2):
            rotate(1, -j)
        if check(2,3):
            if check(3,4):
                rotate(4, j)
            rotate(3, -j)
        rotate(2, j)

    elif i == 3:
        if check(2, 3):
            if check(1, 2):
                rotate(1, j)
            rotate(2, -j)
        if check(3, 4):
            rotate(4, -j)
        rotate(3, j)
    elif i == 4:
        if check(3,4):
            if check(2,3):
                if check(1,2):
                    rotate(1,-j)
                rotate(2,j)
            rotate(3, -j)
        rotate(4, j)
ans = 0
for i in range(4):
    ans += lst_table[i][0] * (2**i)
print(ans)