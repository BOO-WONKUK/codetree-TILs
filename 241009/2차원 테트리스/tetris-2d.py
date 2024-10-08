k = int(input())
lst_command = [list(map(int, input().split())) for _ in range(k)]

lst_yellow = [[0]*4 for _ in range(6)]
lst_red = [[0]*4 for _ in range(6)]

def push_down(color,num):
    if color == 0: # yellow
        lst_yellow.pop(num)
        lst_yellow.insert(0,[0,0,0,0])
    elif color == 1: # red
        lst_red.pop(num)
        lst_red.insert(0,[0,0,0,0])


def check_full():
    global score
    # yellow 체크
    for i in range(5,1,-1):
        if sum(lst_yellow[i]) == 4:
            push_down(0,i)
            score += 1
    for i in range(0,2):
        cnt_yel = 0
        for j in range(4):
            if lst_yellow[i][j] == 1:
                push_down(0,5)



    # red 체크
    for i in range(5, 1, -1):
        if sum(lst_red[i]) == 4:
            push_down(1,i)
            score += 1
    for i in range(0,2):
        cnt_red = 0
        for j in range(4):
            if lst_red[i][j] == 1:
                push_down(1,5)



def simulate(t,x,y):
    red_change = {
        0:3,
        1:2,
        2:1,
        3:0
    }
    red_x = y
    red_y = red_change[x]
    if t == 1:
        for i in range(0,6):  # 범위 생각 다시
            if i == 5 and lst_yellow[i][y] == 0:
                lst_yellow[i][y] = 1
                break
            if lst_yellow[i][y] == 1:
                lst_yellow[i-1][y] = 1
                break

        for i in range(0,6):
            if i == 5 and lst_red[i][red_y] == 0:
                lst_red[i][red_y] = 1
                break
            if lst_red[i][red_y] == 1:
                lst_red[i-1][red_y] = 1
                break

    if t == 2:
        for i in range(0, 6):  # yellow
            if i == 5 and lst_yellow[i][y] == 0 and lst_yellow[i][y+1] == 0:
                lst_yellow[i][y] = 1
                lst_yellow[i][y+1] = 1
                break
            if lst_yellow[i][y] == 1 or lst_yellow[i][y+1] == 1:
                lst_yellow[i - 1][y] = 1
                lst_yellow[i - 1][y+1] = 1
                break

        for i in range(0, 6):  # red
            if i == 5 and lst_red[i][red_y] == 0 and lst_red[i-1][red_y] == 0:
                lst_red[i][red_y] = 1
                lst_red[i-1][red_y] = 1
                break
            if lst_red[i][red_y] == 1:
                lst_red[i - 1][red_y] = 1
                lst_red[i - 2][red_y] = 1
                break

    if t == 3:
        for i in range(0, 6):  # 범위 생각 다시
            if i == 5 and lst_yellow[i][y] == 0 and lst_yellow[i-1][y] == 0:
                lst_yellow[i][y] = 1
                lst_yellow[i-1][y] = 1
                break
            if lst_yellow[i][y] == 1:
                lst_yellow[i - 1][y] = 1
                lst_yellow[i - 2][y] = 1
                break

        for i in range(0, 6):
            if i == 5 and lst_red[i][red_y] == 0 and lst_red[i][red_y-1] == 0:
                lst_red[i][red_y] = 1
                lst_red[i][red_y-1] = 1
                break
            if lst_red[i][red_y] == 1 or lst_red[i][red_y-1] == 1:
                lst_red[i-1][red_y] = 1
                lst_red[i-1][red_y-1] = 1
                break

score = 0
for t,x,y in lst_command:
    simulate(t,x,y)
    check_full()
print(score)
ans = 0


for l in [lst_red,lst_yellow]:
    for o in l:
        ans += sum(o)
print(ans)