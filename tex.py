# def print_formatted(number):
#     width = len(bin(number)[2:])
#     for i in range(1, number+1):
#         deci = str(i)
#         octa = oct(i)[2:]
#         hexa = hex(i)[2:].upper()
#         bina = bin(i)[2:]
#         print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

# print_formatted(17)


# def print_formatted(number):

#     width = len("{0:b}".format(number))

#     for i in range(1, number + 1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

# # if __name__ == '__main__':
# #     n = int(input())
# print_formatted(17)


def generate_pyramid(size):
    if size < 1:
        return "Size must be 1 or greater."

    def get_char(i):
        return chr(ord('a') + i)

    pyramid = []
    width = (size - 1) * 4 + 1

    for i in range(size):
        row = []
        for j in range(size - i - 1):
            row.append('-')
        for k in range(i + 1):
            row.append(get_char(size - k - 1))
            if k < i:
                row.append('-')
        for l in range(i):
            row.append(get_char(size - l - 1))
            if l < i - 1:
                row.append('-')

        pyramid.append(''.join(row).center(width, '-'))

    return '\n'.join(pyramid)

# Teste para o tamanho 3
size = 3
result = generate_pyramid(size)
print(result)


def generate_pyramid(size):
    if size < 1:
        return "Size must be 1 or greater."

    def get_char(i):
        return chr(ord('a') + i)

    pyramid = []
    width = (size - 1) * 4 + 1

    for i in range(size):
        row = ['-'] * (size - i - 1)
        row += [get_char(size - j - 1) for j in range(i + 1)]
        row += [get_char(size - k - 1) for k in range(i - 1, -1, -1)]

        pyramid.append(''.join(row).center(width, '-'))

    return '\n'.join(pyramid)

# Teste para o tamanho 3
size = 3
result = generate_pyramid(size)
print(result)
