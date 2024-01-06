# arr = [1, 3, 5, 7, 9]
arr = [7, 69, 2, 221, 8974]
arr = sorted(arr)
maxx = sum(i for i in sorted(arr[len(arr)-4:]))
min = sum(i for i in sorted(arr[:4]))

print(sorted(arr[len(arr)-4:]))
print(min)
print(maxx)


def miniMaxSum(arr):
    arr = sorted(arr)
    maxx = sum(i for i in arr[len(arr)-4:])
    minn = sum(i for i in arr[:4])
    
    print (f"{minn} {maxx}")

print(miniMaxSum(arr))