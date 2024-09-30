n = int(input())
lst = []
result = []
for _ in range(n):
    lst.append(int(input()))
tmp = 0
idx = 0

for i in range(n):
    if tmp == 0:
        tmp = lst[i]

    if tmp <= lst[i]:
        tmp = lst[i]
        continue
    else:
        tmp = lst[i]
        idx = i-1
        break
idx_change = 0
for i in range(n):
    if lst[i] < tmp:
        idx_change = i
    else:
        print(abs(idx_change - idx)-1)
        break