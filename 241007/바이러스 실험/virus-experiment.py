from collections import deque

n, m, k = map(int, input().split())
yang = [[5] * n for _ in range(n)]  # 양분 초기값
yang_plus = [list(map(int, input().split())) for _ in range(n)]  # 매년 추가되는 양분
vir_map = [[deque() for _ in range(n)] for _ in range(n)]  # 각 칸에 있는 나무들(큐로 관리)

# 나무 입력 받기
for _ in range(m):
    r, c, age = map(int, input().split())
    vir_map[r-1][c-1].append(age)

# 방향 배열 (8방향)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate():
    # 봄 & 여름
    for i in range(n):
        for j in range(n):
            if vir_map[i][j]:
                live_trees = deque()  # 살아남을 나무들
                dead_nutrients = 0  # 죽은 나무가 남긴 양분
                
                while vir_map[i][j]:
                    age = vir_map[i][j].popleft()
                    if yang[i][j] >= age:  # 나이가 양분보다 적거나 같으면 성장
                        yang[i][j] -= age
                        live_trees.append(age + 1)
                    else:
                        dead_nutrients += age // 2  # 죽은 나무가 남긴 양분

                yang[i][j] += dead_nutrients  # 여름에 죽은 나무들의 양분 추가
                vir_map[i][j] = live_trees  # 살아남은 나무만 다시 저장

    # 가을 (번식)
    for i in range(n):
        for j in range(n):
            for age in vir_map[i][j]:
                if age % 5 == 0:  # 나이가 5의 배수인 나무만 번식
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            vir_map[nr][nc].appendleft(1)  # 번식하는 나무의 나이는 1

    # 겨울 (양분 추가)
    for i in range(n):
        for j in range(n):
            yang[i][j] += yang_plus[i][j]

# k년 동안 시뮬레이션 실행
for _ in range(k):
    simulate()

# 나무의 총 개수 세기
result = 0
for i in range(n):
    for j in range(n):
        result += len(vir_map[i][j])

print(result)