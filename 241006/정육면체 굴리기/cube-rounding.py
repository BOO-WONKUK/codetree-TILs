n,m,x,y,k = map(int, input().split())
lst_map = [list(map(int, input().split())) for _ in range(n)]
lst_dir = list(map(int, input().split()))
lst_dice = [0 for _ in range(6)]

def move_e():
    global x, y,lst_dice
    sub_dice = [0 for _ in range(6)]
    x += 1
    sub_dice[0] = lst_dice[1]
    sub_dice[1] = lst_dice[5]
    sub_dice[2] = lst_dice[2]
    sub_dice[3] = lst_dice[0]
    sub_dice[4] = lst_dice[4]
    sub_dice[5] = lst_dice[3]
    lst_dice = sub_dice[:]
def move_w():
    global x, y, lst_dice
    sub_dice = [0 for _ in range(6)]
    x -= 1
    sub_dice[0] = lst_dice[3]
    sub_dice[1] = lst_dice[0]
    sub_dice[2] = lst_dice[2]
    sub_dice[3] = lst_dice[5]
    sub_dice[4] = lst_dice[4]
    sub_dice[5] = lst_dice[1]
    lst_dice = sub_dice[:]
def move_n():
    global x, y, lst_dice
    sub_dice = [0 for _ in range(6)]
    y -= 1
    sub_dice[0] = lst_dice[2]
    sub_dice[1] = lst_dice[1]
    sub_dice[2] = lst_dice[5]
    sub_dice[3] = lst_dice[3]
    sub_dice[4] = lst_dice[0]
    sub_dice[5] = lst_dice[4]
    lst_dice = sub_dice[:]
def move_s():
    global x, y, lst_dice
    sub_dice = [0 for _ in range(6)]
    y += 1
    sub_dice[0] = lst_dice[4]
    sub_dice[1] = lst_dice[1]
    sub_dice[2] = lst_dice[0]
    sub_dice[3] = lst_dice[3]
    sub_dice[4] = lst_dice[5]
    sub_dice[5] = lst_dice[2]
    lst_dice = sub_dice[:]

for i in lst_dir:
    if (x == m-1 and i == 1) or (x == 0 and i == 2) or (y == 0 and i == 3) or (y == n-1 and i == 4) :
        continue
    if i == 1:
        move_e()
    elif i == 2:
        move_w()
    elif i == 3:
        move_n()
    else:
        move_s()
    if lst_map[y][x] == 0:
        lst_map[y][x] = lst_dice[5]
    else:
        lst_dice[5] = lst_map[y][x]
        lst_map[y][x] = 0
    print(lst_dice[0])