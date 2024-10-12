n,m,k = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
people = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    people[i].append(1)
ans = 0
chul_x,chul_y = map(int, input().split())

dx,dy = [0,0,-1,1],[-1,1,0,0] # 좌 우 상 하

def in_range(i,j):
    if 1<=i<=n and 1<=j<=n:
        return True
    return False

def rotate(i,j,wh):
    global chul_x,chul_y

    miro[chul_x-1][chul_y-1] = -100
    # for idxx in range(m):
    #     px,py,pp = people[idxx][0],people[idxx][1],people[idxx][2]
    #     if pp == 1:
    #         miro[px-1][py-1] = (idxx+1)*-1
    osub_miro = []
    for q in range(i,i+wh):
        osub_miro.append(miro[q][j:j+wh])
    # for x in range(j,j+wh):           # 미로 회전
    #     tmp = []
    #     for k in range(i+wh-1,i-1,-1):
    #         tmp.append(miro[k][x])
    #     sub_miro.append(tmp)
    sub_miro = [qqq[:] for qqq in osub_miro]
    people_tmp= []
    for x in range(wh):
        for y in range(wh):
            sub_miro[x][y] = osub_miro[wh-y-1][x]
            for cntt,(aa,bb,cc) in enumerate(people):
                if (wh-y-1,x,1) == (aa-i-1,bb-j-1,cc):
                    people_tmp.append([cntt,i+x+1,j+y+1,1])
    for a,b,c,d in people_tmp:
        people[a] = [b,c,d]
    for x in range(wh):                 # 벽 내구도 감소
        for y in range(wh):
            if sub_miro[x][y] > 0:
                sub_miro[x][y] -= 1
    for x in range(wh):           # 미로 갱신
        for y in range(wh):
            miro[i + x][j + y] = sub_miro[x][y]
    for ii in range(n):
        for jj in range(n):
            if miro[ii][jj] == -100:
                chul_x, chul_y = ii + 1, jj + 1
                miro[ii][jj] = 0
            # elif miro[ii][jj] < 0:
            #     tmpp = miro[ii][jj] * -1 - 1
            #     miro[ii][jj] = 0
            #     people[tmpp][0],people[tmpp][1] = ii+1,jj+1


for turn in range(k):
    # 참가자 이동
    for num in range(m):
        if people[num][2] == 0: continue

        pi, pj = people[num][0], people[num][1]
        if (chul_x,chul_y) == (pi,pj):
            people[num][2] = 0
            continue
        mn_dist = abs(chul_x-pi) + abs(chul_y - pj)
        mn_idx = -1
        for idx_dir in range(3,-1,-1):
            ni,nj = pi+dx[idx_dir], pj+dy[idx_dir]
            if in_range(ni, nj) and miro[ni-1][nj-1] == 0:
                ndist = abs(chul_x-ni) + abs(chul_y-nj)
                if ndist < mn_dist:
                    mn_dist = ndist
                    mn_idx = idx_dir

        if mn_idx == -1:    # 이동불가
            continue
        else:               # 이동가능
            ans += 1
            ni,nj = pi +dx[mn_idx], pj + dy[mn_idx]
            if (chul_x,chul_y) == (ni,nj):
                people[num][2] = 0
            else:
                people[num][0], people[num][1] = ni, nj

    die_cnt = 0
    for a, b, c in people:
        if c == 0:
            die_cnt += 1
    if die_cnt == m:
        break

    # 미로 회전
    lst_box = []
    for mx_wh in range(2,n+1):
        for i in range(n-mx_wh+1):
            for j in range(n-mx_wh+1):
                chul_tmp = 0
                people_tmp = 0
                for w in range(mx_wh):
                    for h in range(mx_wh):
                        if (chul_x,chul_y) == (i+h+1,j+w+1):
                            chul_tmp += 1
                        elif [i+h+1,j+w+1,1] in people:
                            people_tmp += 1
                if chul_tmp >= 1 and people_tmp >= 1:
                    lst_box.append([i,j,mx_wh])         # 좌상단 좌표, 가로세로 너비
        if len(lst_box) > 0:
            lst_box.sort(key = lambda x:(x[0],x[1],x[2]))
            ro_i, ro_j, ro_wh = lst_box[0]
            rotate(ro_i,ro_j,ro_wh)
            break




# 정답 출력
print(ans)
print(chul_x,chul_y)