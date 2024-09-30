n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
sort_lst = sorted(lst)
tmp = 0
idx = -1 

for i in range(1, n):
    if lst[i] < lst[i - 1]:
        idx = i  
        break

if idx != -1:
    swap_idx = sort_lst.index(lst[idx])

    result = abs(swap_idx - idx) -1 
    print(result)
else:
    print(0)