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
n = 12
# resto = n
# while resto !=0:
#     for i in range(2,n):
#         if n % i == 0:
#             quociente = n // i


print(24%2)
print(24//2)


def factor(n):
    "Prime factors of n."
    # factor(99) --> 3 3 11
    # factor(1_000_000_000_000_007) --> 47 59 360620266859
    # factor(1_000_000_000_000_403) --> 1000000000000403
    for prime in sieve(math.isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n