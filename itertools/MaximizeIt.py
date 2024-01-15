

# mumeroListaes = 3
# M = 1000
# l1 = [2, 5, 4]
# l2 = [3, 7, 8, 9]
# l3 = [5, 5, 7, 8, 9, 10]




# lp1 = [(x**2)%M for x in l1]
# lp2 = [(x**2)%M for x in l2]
# lp3 = [(x**2)%M for x in l3]
import itertools

aux = []
k, m = map(int, input().split())
for i in range(k):
    numbers = list(map(int, input().split()))[1:]
    aux.append(numbers)
    
max_modulo = 0

for combination in itertools.product(*aux):
    modulo_result = sum(x ** 2 for x in combination) % m
    max_modulo = max(max_modulo, modulo_result)

print(max_modulo)


# prod = itertools.product(*aux)

# maior = 0
# for i in prod:
#     maior = max(maior,sum(i))
        
# print(maior)
    
    
    
    # aux1 = []
    # aux1 = (map(int, input().split()))
    # aux2 = []
    # aux2 = [(x**2)%m for x in aux1]
    # aux.append(aux2)