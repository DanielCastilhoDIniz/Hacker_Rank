"""
This problem is a programming version of Problem 3 from projecteuler.net

The prime factors of  are  and .

What is the largest prime factor of a given number ?

Input Format

First line contains , the number of test cases. This is followed by  lines each containing an integer .

Constraints

Output Format

For each test case, display the largest prime factor of .

Sample Input 0

2
10
17
Sample Output 0

5
17
Explanation 0

Prime factors of  are , largest is .
Prime factor of  is  itself, hence largest is .
"""
# n = 12
# # resto = n
# # while resto !=0:
# #     for i in range(2,n):
# #         if n % i == 0:
# #             quociente = n // i


# print(24%2)
# print(24//2)


# def factor(n):
#     "Prime factors of n."
#     # factor(99) --> 3 3 11
#     # factor(1_000_000_000_000_007) --> 47 59 360620266859
#     # factor(1_000_000_000_000_403) --> 1000000000000403
#     for prime in sieve(math.isqrt(n) + 1):
#         while not n % prime:
#             yield prime
#             n //= prime
#             if n == 1:
#                 return
#     if n > 1:
#         yield n
import time
start = time.time()
primo = [1,2,3,5]
for n in range(2, 30):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        primo.append(n)

end = time.time()
laeps= start - end
print(primo)
print(laeps)


def crivo_eratostenes(N):
    primos = []
    numeros = [True] * (N + 1)
    for i in range(2, int(N**0.5) + 1):
        if numeros[i]:
            primos.append(i)
            for j in range(i*i, N+1, i):
                numeros[j] = False
    for i in range(int(N**0.5) + 1, N+1):
        if numeros[i]:
            primos.append(i)
    return primos

limite_superior = 30
primos_ate_limite = crivo_eratostenes(limite_superior)
print(primos_ate_limite)

# com retorno do primos
def prime_checker(number):
  primo = []
  for n in range(1, number+1):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        primo.append(n)
  if number in primo:
    print("It's a prime number.")
   
  else:
    print("It's not a prime number.")
    
prime_checker(13)


def prime_checker(number):
  is_primo = True
  for n in range(2, number):
    if number % n == 0:
        is_primo = False
  if is_primo:
    print("It's a prime number.")
   
  else:
    print("It's not a prime number.")
    
prime_checker(13)