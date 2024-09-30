a = input().strip()
b = input().strip()

int_a = int(a, 2)
int_b = int(b, 3)

for i in range(len(a)):
    for j in range(len(b)):
        a_plus = int_a + (2**i) 
        a_minus = int_a - (2**i)
        
        b_plus = int_b + (3 ** j)
        b_minus = int_b - (3 ** j)
        
        if a_plus == b_plus or a_plus == b_minus:
            print(a_plus)
            exit()
        elif a_minus == b_plus or a_minus == b_minus:
            print(a_minus)
            exit()