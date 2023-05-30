INPUT_STRING = "1100010111111100011101010100011010011010111000000101010001000101"
BINARY = True

def va_to_pa(s, binary_flag):
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
    if binary_flag:
        return "These are the index positions for each pagetable converted in binary: " + str(binary_arr)
    else:
        return "These are the index positions for each pagetable not in binary: " + str(pg_table_arr)

     


def binary_to_decimal(binary):
    dec = 0
    for digit in binary:
        dec = dec*2 + int(digit)
    return dec


print(va_to_pa(INPUT_STRING, BINARY))