"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format

A single integer denoting .

Constraints

Sample Input
"""


def print_formatted(number):

    def decimal_to_octal(decimal):
        octal = ""
        while decimal > 0:
            remainder = decimal % 8
            octal = str(remainder) + octal
            decimal //= 8
        return octal if octal else "0"

    def decimal_to_hex(decimal):
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal //= 16
        return hexadecimal

    def decimal_to_binario(decimal):
        binario = ""
        while decimal > 0:
            remainder = decimal % 2
            binario = str(remainder) + binario
            decimal //= 2
        return binario

    # Calcula a largura máxima para a formatação
    width = len("{0:b}".format(number))

    # Loop de 1 até o número fornecido
    for i in range(1, number+1):
        # Converte cada número para sua representação e ajusta a largura
        dec = str(i).rjust(width)
        octal = decimal_to_octal(i).rjust(width)
        hexa = decimal_to_hex(i).rjust(width)
        binario = decimal_to_binario(i).rjust(width)

        # Imprime os números formatados
        print(f'{dec} {octal} {hexa} {binario}')


# Exemplo de uso com number = 17
number = 17
print_formatted(number)


print(print_formatted(17))


# print(print_formatted(number))


# binario = ""
# decimal = number
# while decimal > 0:
#     remainder = decimal % 2
#     binario = str(remainder) + binario
#     decimal //= 2
# print(binario)

# decimal to octal lento
# def decimal_to_octal(number):
#     aux = []
#     while number > 0:
#         number, reminder = divmod(number, 8)
#         aux.append(reminder)
#     octal = (int("".join(map(str, sorted(aux)))))
#     return octal

# decimal to octal lento
# print(divmod(number, 8))
# aux = []
# while True:
#     if number == 0:
#         break
#     else:
#         aux.append(number % 8)
#         number = number // 8
# aux2 = (int("".join(map(str, sorted(aux)))))

# def octal_to_decimal(number):

#     decimal_octal = 0
#     temp = number  # Mantém uma cópia do número original

#     # Calcula o número decimal
#     for i in range(len(str(number))):
#         digit = temp % 10
#         decimal_octal += digit * 8**i
#         temp //= 10
# number = 236

# print(hex(number))

#     return decimal_octal lento
# dict_aux = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
# hex_digits = "0123456789ABCDEF"
# aux = []

# while number > 0:
#     number, reminder = divmod(number, 16)
#     if reminder in dict_aux and 10 <= reminder <= 15:
#         aux.append(dict_aux[reminder])
#     elif reminder > 15:
#         aux.append(reminder + 10)
#     else:
#         aux.append(reminder)

# hexx = (("".join(map(str, reversed(aux)))))

# print(aux,hexx)


# def decimal_to_hex(decimal):
#     hex_digits = "0123456789ABCDEF"
#     hexadecimal = ""

#     while decimal > 0:
#         remainder = decimal % 16
#         hexadecimal = hex_digits[remainder] + hexadecimal
#         decimal //= 16

#     return hexadecimal

# # Exemplo de uso
# decimal_input = 236
# hexadecimal_output = decimal_to_hex(decimal_input)
# print(f"O valor hexadecimal de {decimal_input} é {hexadecimal_output}")

# hex_digits = "0123456789ABCDEF"
# decimal =236
# result = ""
# while decimal > 0:
#     remainder = decimal % 16
#     result = hex_digits[remainder] + result
#     decimal //= 16
#     print(decimal)


# otimo
# def print_formatted(number):

#     width = len("{0:b}".format(number))

#     for i in range(1, number + 1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# def decimal_to_binario(decimal):
#     binario = ""
#     # decimal = number
#     while decimal > 0:
#         remainder = decimal % 2
#         binario = str(remainder) + binario
#         decimal //= 2
#     return binario

# print(decimal_to_binario(10))
