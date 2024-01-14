from itertools import groupby, combinations_with_replacement, combinations,chain

len_list = int(input())
letters = input().split()
agrup = int(input())
comb =list(combinations(letters,agrup))
contagem = 0
# Conta as ocorrências de cada letra
for i in comb:
    if "a" in i:
        contagem += 1
# print(contagem)
# print(len(comb))

print(contagem/(len(comb)))


#mode  2
n, s, k = int(input()), input().split(), int(input())
res = sum('a' in tu for tu in combinations(s, k)) / len(tuple(combinations(s, k)))
print(f"{res:.4f}")



