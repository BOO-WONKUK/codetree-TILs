n = int(input())
lst = []
result = []
for _ in range(n):
    lst.append(int(input()))
sort_lst = sorted(lst)
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

print(abs(sort_lst.index(tmp) - idx))