n,m,p,c,d = map(int, input().split())
rr,rc = map(int, input().split())
lst_san = [[-100,-100]]
lst_tmp_san = [list(map(int, input().split())) for _ in range(p)]
lst_tmp_san.sort(key = lambda x:x[0])
lst_stun_san = []
lst_san_score = [0]*(p+1)
lst_san_die = []
for sn,sr,sc in lst_tmp_san:
    lst_san.append([sr,sc])

ru_dx,ru_dy = [-1,-1,-0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
san_dx,san_dy = [-1,0,1,0],[0,1,0,-1]

def in_range(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    return False

def can_go_san(x,y):
    if [x,y] in lst_san:
        return False
    return True
def sangho(x, y, num, dir):
    # 다음 위치 설정
    nx = x + ru_dx[dir] if num == 0 else x - san_dx[dir]
    ny = y + ru_dy[dir] if num == 0 else y - san_dy[dir]

    # 게임판 안에 있고, 그 위치에 다른 산타가 있는 경우
    if in_range(nx, ny):
        if [nx, ny] in lst_san:
            idx = lst_san.index([nx, ny])  # 해당 산타 인덱스 찾기
            sangho(nx, ny, num, dir)  # 재귀적으로 상호작용 처리

            # 밀려난 산타의 위치 업데이트
            lst_san[idx][0] += ru_dx[dir] if num == 0 else -san_dx[dir]
            lst_san[idx][1] += ru_dy[dir] if num == 0 else -san_dy[dir]
        else:
            # 위치가 비어있다면 현재 산타의 위치를 업데이트
            idx = lst_san.index([x, y])
            lst_san[idx] = [nx, ny]
    else:
        # 게임판 밖으로 나간 경우 산타 제거
        idx = lst_san.index([x, y])
        lst_san_die.append(idx)
        lst_san[idx] = [-100, -100]

# def sangho(x,y,num,dir):
#     if num == 0: # 루 -> 산 8방
#         if not can_go_san(x,y): # 그 좌표에 산타가 없다면 상호작용 X
#             pass
#         else:               # 산타 있다면 상호작용 O
#             idx = lst_san.index([x,y])
#             lst_san[idx][0] += ru_dx[dir]
#             lst_san[idx][1] += ru_dy[dir]
#             x = lst_san[i][0] + ru_dx[dir] if num == 0 else lst_san[i][0] - san_dx[dir]
#             y = lst_san[i][1] + ru_dy[dir] if num == 0 else lst_san[i][1] - san_dy[dir]
#             sangho(x,y,num,dir)
#
#     elif num == 1: # 산 -> 루 4방
#         if not can_go_san(x,y): # 그 좌표에 산타가 없다면 상호작용 X
#             pass
#         else:               # 산타 있다면 상호작용 O
#             idx = lst_san.index([x,y])
#             lst_san[idx][0] -= san_dx[dir]
#             lst_san[idx][1] -= san_dy[dir]
#             x = lst_san[i][0] + ru_dx[dir] if num == 0 else lst_san[i][0] - san_dx[dir]
#             y = lst_san[i][1] + ru_dy[dir] if num == 0 else lst_san[i][1] - san_dy[dir]
#             sangho(x, y, num, dir)

# def sangho(x, y, who, dir):
#     nx = lst_san[i][0] + ru_dx[dir] if who == 0 else lst_san[i][0] - san_dx[dir]
#     ny = lst_san[i][1] + ru_dy[dir] if who == 0 else lst_san[i][1] - san_dy[dir]
#
#     # 다음 위치가 맵 안에 있고 비어있는지 확인
#     if in_range(nx, ny):
#         if [nx, ny] in lst_san:  # 새 위치에 또 다른 산타가 있을 경우
#             # 재귀적으로 다음 산타 충돌 처리
#             sangho(nx, ny, 1, dir)
#         else:
#             lst_san[i] = [nx, ny]  # 산타를 새로운 위치로 이동
#     else:
#         lst_san_die.append(i)  # 맵 밖으로 나가면 산타 제거
#         lst_san[i] = [-100, -100]  # 맵 밖으로 간 산타의 위치를 유효하지 않은 값으로 설정


def crush_ru_san(dir): # 루돌프가 산타한테 충돌
    global turn, c
    for i in range(1,p+1):
        if i not in lst_san_die:
            if rr == lst_san[i][0] and rc == lst_san[i][1]:
                lst_stun_san.append((i,turn))
                lst_san_score[i] += c
                idx = i
                nx = lst_san[idx][0] + (ru_dx[dir] * c)
                ny = lst_san[idx][1] + (ru_dy[dir] * c)
                if in_range(nx,ny):
                    if [nx,ny] in lst_san:
                        sangho(nx,ny,0,dir)
                        lst_san[idx][0] = nx
                        lst_san[idx][1] = ny
                    else:
                        lst_san[idx][0] = nx
                        lst_san[idx][1] = ny
                else:
                    lst_san_die.append(idx)
                    lst_san[idx] = [-100,-100]

def crush_san_ru(dir):  # 산타가 루돌프한테 충돌
    global d
    for i in range(1,p+1):
        if i not in lst_san_die:
            if rr == lst_san[i][0] and rc == lst_san[i][1]:
                lst_stun_san.append((i,turn))
                lst_san_score[i] += d
                idx = i
                nx = lst_san[idx][0] - (san_dx[dir[i-1]] * d)
                ny = lst_san[idx][1] - (san_dy[dir[i-1]] * d)
                if in_range(nx,ny):
                    if [nx,ny] in lst_san:
                        sangho(nx,ny,1,dir[i-1])
                        lst_san[idx][0] = nx
                        lst_san[idx][1] = ny
                    else:
                        lst_san[idx][0] = nx
                        lst_san[idx][1] = ny

                else:
                    lst_san_die.append(idx)
                    lst_san[idx] = [-100,-100]


def rudol():
    global rr,rc
    goal_san = -1
    goal_san_distance = 1e9

    # 가장 가까운 산타 고르기
    for idx in range(1,p+1):
        if idx not in lst_san_die:
            dis =(lst_san[idx][0]-rr)**2 + (lst_san[idx][1] - rc)**2
            if dis < goal_san_distance:
                goal_san = idx
                goal_san_distance = dis
            elif dis == goal_san_distance:
                if lst_san[goal_san][0] < lst_san[idx][0]:
                    goal_san = idx
                elif lst_san[goal_san][0] == lst_san[idx][0]:
                    if lst_san[goal_san][1] < lst_san[idx][1]:
                        goal_san = idx

    # 8방 돌진
    goal_sr = lst_san[goal_san][0]
    goal_sc = lst_san[goal_san][1]
    sub_r = goal_sr - rr
    sub_c = goal_sc - rc
    ru_dir = -1
    if sub_r == 0 and sub_c != 0:
        if sub_c < 0:    # 좌
            ru_dir = 6
        else:               # 우
            ru_dir = 2
    elif sub_r != 0 and sub_c == 0:
        if sub_r > 0:    # 하
            ru_dir = 4
        else:               # 상
            ru_dir = 0
    elif sub_r > 0 and sub_c > 0:   # 우하
        ru_dir = 3
    elif sub_r > 0 and sub_c < 0:   # 좌하
        ru_dir = 5
    elif sub_r < 0 and sub_c > 0:   # 우상
        ru_dir = 1
    elif sub_r < 0 and sub_c < 0:   # 우하
        ru_dir = 7
    rr += ru_dx[ru_dir]
    rc += ru_dy[ru_dir]

    return ru_dir # 루돌프 방향

def santa():
    global rr, rc
    lst_dir_idx = []
    sub_stun = []
    for w,e in lst_stun_san:
        sub_stun.append(w)

    for san_num in range(1,p+1):
        if san_num not in sub_stun and san_num not in lst_san_die:
            sr = lst_san[san_num][0]
            sc = lst_san[san_num][1]
            sub_r = rr - sr
            sub_c = rc - sc
            dir_idx = -1
            min_dir = (sub_r**2 + sub_c**2)
            for i in range(4):
                nx = sr + san_dx[i]
                ny = sc + san_dy[i]
                if in_range(nx,ny) and can_go_san(nx,ny):
                    if min_dir > ((nx-rr)**2 + (ny-rc)**2):
                        min_dir = ((nx-rr)**2 + (ny-rc)**2)
                        dir_idx = i
            if dir_idx != -1:
                lst_dir_idx.append(dir_idx)
                lst_san[san_num][0] += san_dx[dir_idx]
                lst_san[san_num][1] += san_dy[dir_idx]
            else:
                lst_dir_idx.append(-1)
        else:
            lst_dir_idx.append(-1)
    return lst_dir_idx


for turn in range(m):
    for stun_san,cnt_turn in reversed(lst_stun_san):
        if turn >= cnt_turn+2:
            lst_stun_san.remove((stun_san,cnt_turn))
    ru_dir = rudol()
    crush_ru_san(ru_dir)

    # map_ = [[0] * 5 for _ in range(5)]
    # for iii in range(1, p + 1):
    #     if in_range(lst_san[iii][0], lst_san[iii][1]):
    #         map_[lst_san[iii][0] - 1][lst_san[iii][1] - 1] = iii
    #     map_[rr - 1][rc - 1] = -1
    # for kkk in map_:
    #     print(*kkk)
    # print()

    san_dir = santa()
    crush_san_ru(san_dir)
    if len(lst_san_die) == p:
        break
    for i in range(1, p+1):
        if i not in lst_san_die:
            lst_san_score[i] += 1
    # map_ = [[0]*5 for _ in range(5)]
    # for iii in range(1,p+1):
    #     if in_range(lst_san[iii][0],lst_san[iii][1]):
    #         map_[lst_san[iii][0]-1][lst_san[iii][1]-1] = iii
    #     map_[rr-1][rc-1] = -1
    # for kkk in map_:
    #     print(*kkk)
    #
    # print('턴',turn+1)
    # print(rr, rc)
    # print('lst san', lst_san)
    # print('stun', lst_stun_san)
    # print('die',lst_san_die)
    # print('score',lst_san_score)
    # print('--------------')

lst_san_score.pop(0)
print(' '.join(map(str, lst_san_score)))