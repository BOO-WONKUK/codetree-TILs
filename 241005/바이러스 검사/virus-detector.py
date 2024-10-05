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
    cnt += lst_store[i] // lst_num[1]
    cnt += 1
    
print(cnt)