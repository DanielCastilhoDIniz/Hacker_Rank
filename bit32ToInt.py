
def flippingBits(n):
    binario_32_bits = format(n, '032b')
    new = ""
    for i in binario_32_bits:
        if i == "0":
            new += '1'
        else:
            new += '0'
    return int(new, 2)
