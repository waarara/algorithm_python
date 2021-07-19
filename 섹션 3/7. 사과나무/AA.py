# 사과나무

import sys
sys.stdin = open("./섹션 3/7. 사과나무/in1.txt", "r")


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

res = 0
start = end = n//2
print(n)
print(start)

for i in range(n):  # 0~6까지
    for j in range(start, end + 1):
        res += grid[i][j]
        # print(res)
    if i < n//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(res)