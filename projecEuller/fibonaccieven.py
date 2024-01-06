import math
import time
"""calcular soma dos numeros pares sequencia de fibonacci até que valor seja menor que o valor do elemento n qualquer dado. """

#melhor solução
n = 4000000  

a, b = 1, 2
soma = 0

while b <= n:
    
    if b % 2 == 0:
        soma += b
    a, b = b, a + b

print(soma)

print("============"*4)

# solução lenta
start_time = time.time()
n = 10000
s = [1, 2]
for i in range(2, n):
    s.append(s[(i-1)] + s[i-2])

soma = 0
for pos in s:
    if pos % 2 == 0 and soma < n:
        soma += pos
        if soma > n:
            soma -= pos
print(soma)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time:.9f} segundos")
print("============"*4)

# otima solução
x1 = 1
x2 = 2
n = 10000
answer = 0
while x2 <= n:
    start_time = time.time()
    if x2 % 2 == 0:
        answer += x2
    x3 = x1+x2
    x1 = x2
    x2 = x3
print(answer)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time:.9f} segundos")
print("============"*4)





# qualquer elemento da sequencia de posição n, (obs  soma acumulada até n) OverflowError
# n = 10000
# soma2= 0
# for nun in range(0,n,3):
#     start_time = time.time()
#     f_n = round(((1/(math.sqrt(5)))*((1+math.sqrt(5))/2)**nun) - ((1/(math.sqrt(5)))*((1 - math.sqrt(5))/2)**nun))
#     if f_n % 2 == 0 and f_n < n:
#         soma2 += f_n
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Tempo de execução: {elapsed_time} segundos")
# print(round(soma2))
