from collections import defaultdict


# d = defaultdict(list)

# d['python'].append("awesome")

# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

from collections import defaultdict

n, m = map(int, (input().split()))
aux = defaultdict(list)

for i in range(1, n+1):
    aux[input()].append(i)
    print(aux)

for _ in range(m):
    word = input()
    print(*aux[word] if aux[word] else [-1])

print(aux)




