from itertools import combinations

s, k = input().split()
letters = sorted(s)

for i in range(1, int(k) + 1):
    for combination in combinations(letters, i):
        print("".join(combination))