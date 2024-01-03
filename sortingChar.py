# def sorting_char(s):
#     return s[::-1]

# print(sorting_char("Sorting123"))


s = "Sorting1234"
# digits = "0123456789"
# aux = []
# # lista mista
# # mixed_list = [int(i) if i.isdigit() else i for i in s]
# digits_even = [int(i) for i in s if i.isdigit() and int(i) % 2 == 0]
# digits_odd = [int(i) for i in s if i.isdigit() and int(i) % 2 != 0]
# no_digits_upper = [i for i in s if not i.isdigit() and i.isupper()]
# no_digits_lower = [i for i in s if not i.isdigit() and i.islower()]

# for i in reversed(no_digits_lower):
#     aux.append(i)
# for i in reversed(no_digits_upper):
#     aux.append(i)
# for i in digits_odd:
#     aux.append(str(i))
# for i in digits_even:
#     aux.append(str(i))
# result =""
# for i in aux:
#     result += "".join(str(i))

# print(result)
# print((no_digits_upper))
# print((no_digits_lower))
# print((digits_even))
# print((digits_odd))

# for i in range(len(no_digits)):
# for caractere in no_digits:
#     if caractere.islower():
#         aux.append(caractere)
#     if  caractere.isupper():
#         aux[len(no_digits)] = caractere
# print(aux)


# print (digits, no_digits)
# for char in mixed_list:
#     if mixed_list[char]
#         aux.append(mixed_list[char])


# print((mixed_list))
# print((aux))
# # print (type((liststring[-1])))
# # print (type((liststring[1])))


def sorting_char(s):
    aux = []
    digits_even = [int(i) for i in s if i.isdigit() and int(i) % 2 == 0]
    digits_odd = [int(i) for i in s if i.isdigit() and int(i) % 2 != 0]
    no_digits_upper = [i for i in s if not i.isdigit() and i.isupper()]
    no_digits_lower = [i for i in s if not i.isdigit() and i.islower()]

    for i in sorted(no_digits_lower):
        aux.append(i)
    for i in sorted(no_digits_upper):
        aux.append(i)
    for i in digits_odd:
        aux.append(str(i))
    for i in digits_even:
        aux.append(str(i))
    result =""
    for i in aux:
        result += "".join(str(i))

    return(result)

    


# s = input()
# print(sorting_char(s))
 
#pythonico
def sorting_char(s):
    # Organiza os caracteres na ordem especificada
    sorted_chars = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.lower()))

    # Converte os caracteres ordenados de volta para uma string
    result = ''.join(sorted_chars)

    return result, sorted_chars

print(sorting_char("Sorting1234"))
# if __name__ == '__main__':
#     s = input("Digite uma string: ")
#     print(sorting_char(s))
