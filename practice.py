def count_bits(n):
    binary_str = str(format(n, "b"))
    i = 0
    for int in binary_str:
        if int == "1":
            i += 1
    return i 


print(count_bits(10))