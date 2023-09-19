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
