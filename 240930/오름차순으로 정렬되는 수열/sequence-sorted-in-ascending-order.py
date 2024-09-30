n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
sort_lst = sorted(lst)
for i in range(n):
    if lst[i] != sort_lst[i]:
        tmp = sort_lst[i]
        break
print(lst.index(tmp) - i - 1)