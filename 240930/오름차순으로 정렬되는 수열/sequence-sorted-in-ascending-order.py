n = int(input())
lst = [int(input()) for _ in range(n)]
sort_lst = sorted(lst)

diff_lst = []

for i in range(n):
    if lst[i] != sort_lst[i]:
        diff_lst.append(i)

if len(diff_lst) == 0:
    print(0)
elif len(diff_lst) == 2:
    print(1)
else:
    print(len(diff_lst) // 2 + 1)