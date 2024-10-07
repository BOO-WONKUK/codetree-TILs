n,m,k = map(int, input().split())
yang = [[5]*n for _ in range(n)]
yang_plus = [list(map(int, input().split())) for _ in range(n)]
vir = []
for _ in range(m):
    r,c,age = map(int, input().split())
    vir.append([r-1,c-1,age])

def is_range(r,c):
    if 0<=r<=4 and 0<=c<=4:
        return True
    return False

def simulate():
    vir.sort(key = lambda x : x[2])
    lst_del = []
    for i in range(len(vir)):
        r = vir[i][0]
        c = vir[i][1]
        age = vir[i][2]
        if yang[r][c] >= age:
            yang[r][c] -= age
            vir[i][2] += 1
        else:
            lst_del.append(i)
    for i in lst_del:
        yang[vir[i][0]][vir[i][1]] += vir[i][2]//2
    for i in reversed(lst_del):
        del vir[i]
    for i in range(len(vir)):
        r = vir[i][0]
        c = vir[i][1]
        age = vir[i][2]
        if age % 5 == 0:
            for k in range(-1,2):
                for l in range(-1,2):
                    if is_range(r+k,c+l):
                        if l==0 and k == 0:
                            pass
                        else:
                            vir.append([r+k,c+l,1])
    for i in range(n):
        for j in range(n):
            yang[i][j] += yang_plus[i][j]

for _ in range(k):
    simulate()

print(len(vir))