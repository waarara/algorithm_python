import sys
sys.stdin = open("./섹션 3/6. 격자판 최대합/input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in a:
    print(i)

largest = -2147000000

for i in range(n):
    sumrow = sumcol = 0
    for j in range(n):
        sumrow += a[i][j]
        sumcol += a[j][i]

    if sumrow > largest:
        largest = sumrow
    if sumcol > largest:
        largest = sumcol

print(largest)

sumrow = sumcol = 0

for i in range(n):
    sumrow += a[i][n+i]
    sumcol += a[i][n-i-1]

if sumrow > largest:
    largest = sumrow

if sumcol > largest:
    largest = sumcol

print(largest)