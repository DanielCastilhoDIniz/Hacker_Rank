"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
"""

from itertools import groupby

s = input()
# Usa a função groupby para contar as ocorrências consecutivas de cada dígito na string
# Cria uma lista de tuplas onde o primeiro elemento é o dígito e o segundo é a contagem de ocorrências
t = [(int(k), list(g).count(k)) for k, g in groupby(s)]
print(*t)
