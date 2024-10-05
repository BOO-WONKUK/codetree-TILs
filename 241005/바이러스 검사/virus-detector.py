n = int(input())
lst_store = list(map(int,input().split()))
lst_num = list(map(int, input().split()))

cnt = 0
for i in range(n):
    lst_store[i] -= lst_num[0]
    cnt += 1

for i in range(n):
    if lst_store[i] <= 0 :
        continue
    if lst_store[i] // lst_num[0] > lst_store[i] // lst_num[1]:
        cnt += lst_store[i] // lst_num[1]
        cnt += (lst_store[i] % lst_num[0]) // lst_num[1] + 1
    
    elif lst_store[i] // lst_num[0] < lst_store[i] // lst_num[1]:
        cnt += lst_store[i] // lst_num[0]
        cnt += (lst_store[i] % lst_num[1]) // lst_num[0] + 1
    
print(cnt)