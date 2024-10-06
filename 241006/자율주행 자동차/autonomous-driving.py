n, m = map(int, input().split())
x, y, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문한 셀의 수
visited_count = 0

def can_move(new_x, new_y):
    return 0 <= new_y < n and 0 <= new_x < m and lst[new_y][new_x] == 0  # 벽이 아닌지 확인

def turn_left():
    global d
    d = (d - 1) % 4  # 방향을 왼쪽으로 회전

def back():
    global x, y, d
    back_d = (d - 2) % 4  # 반대 방향
    new_x = x + dx[back_d]
    new_y = y + dy[back_d]
    if can_move(new_x, new_y):  # 뒤로 이동 가능 여부 확인
        x, y = new_x, new_y  # 이동
        return True
    return False  # 이동 불가능

# 시작 위치를 방문한 것으로 처리
lst[y][x] = 2
visited_count += 1

while True:
    can_move_forward = False  # 앞으로 이동할 수 있는지 체크
    for _ in range(4):  # 4방향 탐색
        turn_left()  # 방향을 왼쪽으로 회전
        new_x = x + dx[d]
        new_y = y + dy[d]

        if can_move(new_x, new_y):  # 이동 가능 여부 확인
            x, y = new_x, new_y  # 이동
            lst[y][x] = 2  # 방문 처리
            visited_count += 1  # 방문한 셀 수 증가
            can_move_forward = True  # 이동 가능
            break  # 이동이 가능하므로 반복 종료

    if not can_move_forward:  # 더 이상 이동할 수 없는 경우
        if not back():  # 뒤로 갈 수 없는 경우
            break  # 종료

print(visited_count)