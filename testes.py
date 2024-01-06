x1=1
x2=2
n =2132
answer=0
while x2<=n:
    if x2%2==0:
        answer+=x2
    x3=x1+x2
    x1=x2
    x2=x3
print(answer)