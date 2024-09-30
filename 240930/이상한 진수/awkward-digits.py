a = input().strip()
b = input().strip()

ia = int(a, 2)
ib = int(b, 3)

for i in range(len(a)):
    ma_plus = ia + (1 << (len(a) - 1 - i)) if a[i] == '0' else ia
    ma_minus = ia - (1 << (len(a) - 1 - i)) if a[i] == '1' else ia

    for j in range(len(b)):
        for d in range(3):
            if str(d) != b[j]:
                mb = b[:j] + str(d) + b[j + 1:]
                mb_value = int(mb, 3)

                if ma_plus == mb_value or ma_minus == mb_value:
                    print(ma_plus if ma_plus == mb_value else ma_minus)
                    exit()