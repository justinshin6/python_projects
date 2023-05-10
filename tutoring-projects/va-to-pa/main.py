def va_to_pa(s):
    # 0000'0001'0010'1100'0110'0100'0100'1011'0001'0101'0000'1010'1101'0000'1010'0110

    new_s = s.replace("'", "")
    unused = new_s[0:16]
    l4 = new_s[16:25]
    l3 = new_s[25:34]
    l2 = new_s[34:43]
    l1 = new_s[43:52]
    offset = new_s[52:64]

    pg_table_arr = [l4, l3, l2, l1]
    binary_arr = [0, 0, 0, 0]
    for i in range(len(pg_table_arr)):
        binary_arr[i] = binary_to_decimal(pg_table_arr[i])

    return "These are the index positions for each pagetable: " + str(binary_arr)


def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

print(va_to_pa("0000'0001'0010'1100'0110'0100'0100'1011'0001'0101'0000'1010'1101'0000'1010'0110"))