"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
"""

def plusMinus(arr):

    positive = sum(1 for num in arr if num > 0)
    negative = sum(1 for num in arr if num < 0)
    zero = sum(1 for num in arr if num == 0)

    print(f"{positive/len(arr):.6f}")
    print(f"{negative/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


n = 6
arr = [-4, -3, -9, 0, 4, 1]
positive =0
negative = 0
zero = 0 
for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative +=1
    else:
        zero += 1

# print(f"{positive/n:.6f}")
# print(f"{negative/n:.6f}")
# print(f"{zero/n:.6f}")

print(plusMinus(arr))
# print(arr.count())


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)
