def bin_to_dec(num,sum,i):
    if num == 0:
        return 1
    else:
        s = num%10
        sum = sum + (s*(2**i))
        i = i + 1
        num = num//10
        return bin_to_dec(num,sum,i)

print(bin_to_dec(1011,0,0))

