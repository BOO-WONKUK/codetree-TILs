n = int(input())
lst = []
result = []
for _ in range(n):
    lst.append(int(input()))
sort_lst = sorted(lst)

for i in range(n):
    if lst[i] != sort_lst[i]:
        result.append(i)
print(max(result) - min(result) - 1)