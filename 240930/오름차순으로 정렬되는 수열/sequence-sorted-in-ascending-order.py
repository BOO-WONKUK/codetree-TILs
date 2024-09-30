n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

sort_lst = sorted(lst)

idx = -1
for i in range(1, n):
    if lst[i] < lst[i - 1]:
        idx = i
        break

if idx == -1:
    print(0)
else:
    tmp = lst[idx]  
    correct_pos = sort_lst.index(tmp)  

    print(abs(correct_pos - idx)-1)