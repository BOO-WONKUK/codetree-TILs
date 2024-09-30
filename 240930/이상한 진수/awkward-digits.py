a = input()
b = input()
int_a = int(a,2)
int_b = int(b,3)
sub = abs(int_a - int_b)
tmp = -1
for i in range(len(a)):
    for j in range(len(b)):
        if sub == abs(2**i - 3**j) or sub == 2**i + 3**j:
            tmp = 0
            break
    if tmp == 0:
        break

if int_a + 2**i == int_b + 3**j:
    print(int_a + 2**i)
elif int_a - 2**i == int_b + 3**j:
    print(int_a - 2**i)
elif int_a + 2**i == int_b - 3**j:
    print(int_a + 2**i)
elif int_a - 2**i == int_b - 3**j:
    print(int_a - 2**i)