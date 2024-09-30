n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
sort_lst = sorted(lst)
print(sort_lst)
for i in range(n):
    if lst[i] != sort_lst[i]:
        tmp = sort_lst[i]
        break
# print(abs(lst.index(tmp) - i - 1))