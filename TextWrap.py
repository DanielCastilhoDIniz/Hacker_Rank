"""
ou are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
# import textwrap
# # SOLUÇÃO QUE IMPRIME ULTIMA LINHA EM BRANCO
# def wrap(string, max_width):
#     start = 0
#     text = -(-len(string)//max_width)
#     for i in range(text):
#         end = start + max_width
#         paragraph = string[start:end]
#         if paragraph:
#             print(paragraph)
#         start = end

# if __name__ == '__main__':

#     wrap('danielcastilhodiniz',3)

import textwrap

def wrap(string, max_width):
    paragraph = textwrap.wrap(string,max_width)
    return '\n'.join(paragraph)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
