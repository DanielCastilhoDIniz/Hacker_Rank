"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .

Constraints

It is guaranteed that  is an odd number and that there is one unique element.
, where .
"""

def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i


# a = [34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]

a = [1]

for i in a:
    if a.count(i) == 1:
        print(i)


numero = 3
binario_32_bits = format(numero, '032b')
new = ""


for i in binario_32_bits:
    if i == "0":
        new += '1'
    else:
        new += '0'

print(type(binario_32_bits))

print(f"{numero:032b}")
print(f"{new}")
print(int(new, 2))







