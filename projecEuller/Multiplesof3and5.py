"""
f we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

For each test case, print an integer that denotes the sum of all the multiples of  or  below .

Sample Input 0

2
10
100
Sample Output 0

23
2318
Explanation 0

For , if we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Similarly for , we get .
"""
# t = 5

# lento
# for i in range(1, t+1):
#     tester = (10**i)
#     aux =[]
#     soma = 0
#     for num in range(0, tester):
#         if num % 3 == 0 or num % 5 == 0:
#             soma += num
#     print(soma)

#melhor solução
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    answer = 0
    k = ((n-1)//3)
    answer += 3*k*(k+1)//2
    
    k = (n-1)//5
    answer += 5*k*(k+1)//2
    
    k = (n-1)//15
    answer -= 15*k*(k+1)//2
    print(answer)

# solução falha para alguns casos
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    answer =0
    answer += ((((n-1)//3)*3 + 3)*((n-1)//3))/2
    answer += ((((n-1)//5)*5 + 5)*((n-1)//5))/2
    answer -= ((((n-1)//15)*15 + 15)*((n-1)//15))/2
    #print(answer)

    print(int(answer))
s = [0,1,2,3,4,5,6,7,8,9,10,100,100]
for i,n in enumerate(s):
    # n = int(input().strip())
    answer =0
    answer += ((((n-1)//3)*3 + 3)*((n-1)//3))/2
                
    answer += ((((n-1)//5)*5 + 5)*((n-1)//5))/2
    answer -= ((((n-1)//15)*15 + 15)*((n-1)//15))/2
    #print(answer)

    print(f"{i} {int(answer)}")

# n= 10
# answer = (((n//3)*3 + 3)*(n//3))/2
# answer5 = (((n//5)*5 + 5)*(n//5))/2
# answer15 = (((n//15)*15 + 5)*(n//15))/2

# print(answer15)

# aux =[]
# for i in range(1, t+1):
#     limit = (10**i)
#     aux.append(limit)
# # print(aux)
# for num in aux:

#     soma3n = int(((num-(num%3) +3)/2)*(((num-(num%3)-3)/3) +1))
#     soma5n = int(((num-(num%5) +5)/2)*(((num-(num%5)-5)/5) +1))
#     soma15n = int(((num-(num%15) +15)/2)*(((num-(num%15)-15)/15) +1))


    # print(soma3n +soma5n - soma15n -num)


print(27//3)
print(10%5)
