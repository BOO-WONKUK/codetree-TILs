n,m,k = map(int, input().split())
yang = [[5]*n for _ in range(n)]
yang_plus = [list(map(int, input().split())) for _ in range(n)]
vir = []
for _ in range(m):
    r,c,age = map(int, input().split())
    vir.append([r-1,c-1,age])

def is_range(r,c):
    if 0<=r<=n-1 and 0<=c<=n-1:
        return True
    return False

# def simulate():
#     vir.sort(key = lambda x : x[2])
#     lst_del = []
#     for i in range(len(vir)):
#         r = vir[i][0]
#         c = vir[i][1]
#         age = vir[i][2]
#         if yang[r][c] >= age:
#             yang[r][c] -= age
#             vir[i][2] += 1
#         else:
#             lst_del.append(i)
#     for i in lst_del:
#         yang[vir[i][0]][vir[i][1]] += vir[i][2]//2
#     for i in reversed(lst_del):
#         del vir[i]
#     for i in range(len(vir)):
#         r = vir[i][0]
#         c = vir[i][1]
#         age = vir[i][2]
#         if age % 5 == 0:
#             for k in range(-1,2):
#                 for l in range(-1,2):
#                     if is_range(r+k,c+l):
#                         if l==0 and k == 0:
#                             pass
#                         else:
#                             vir.append([r+k,c+l,1])
#     for i in range(n):
#         for j in range(n):
#             yang[i][j] += yang_plus[i][j]
def simulate():
    vir.sort(key=lambda x: x[2])  # 매번 정렬 필요 없을 경우 제거 고려
    new_vir = []  # 살아남은 나무를 기록할 리스트
    breed_queue = []  # 새로 추가할 나무 위치를 기록할 리스트
    for r, c, age in vir:
        if yang[r][c] >= age:
            yang[r][c] -= age
            age += 1
            new_vir.append([r, c, age])
            if age % 5 == 0:
                breed_queue.append((r, c))
        else:
            yang[r][c] += age // 2  # 죽은 나무 처리
    # 새로운 나무 번식 처리
    for r, c in breed_queue:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (dr, dc) != (0, 0) and is_range(r + dr, c + dc):
                    new_vir.append([r + dr, c + dc, 1])
    # 양분 추가
    for i in range(n):
        for j in range(n):
            yang[i][j] += yang_plus[i][j]
    return new_vir

# 시뮬레이션 실행
for _ in range(k):
    vir = simulate()

print(len(vir))


# for _ in range(k):
#     simulate()

# print(len(vir))