from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

operator_list = []
operator_list += ['+'] * operators[0]
operator_list += ['-'] * operators[1]
operator_list += ['*'] * operators[2]

all_permutations = set(permutations(operator_list))

min_value = 1e9  
max_value = -1e9 

for perm in all_permutations:
    result = numbers[0]
    for i in range(1, n):
        if perm[i-1] == '+':
            result += numbers[i]
        elif perm[i-1] == '-':
            result -= numbers[i]
        elif perm[i-1] == '*':
            result *= numbers[i]
    
    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(int(min_value), int(max_value))