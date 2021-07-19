
# 곳감
import sys
sys.stdin = open("./섹션 3/8. 곳감/input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# for i in a:
#     print(i)

turn = int(input())
# print(turn)

for i in range(turn):
    col , direction, distance = map(int, input().split())
    print(col,direction,distance)

    if direction == 0:
        for x in range(distance):
            a[col - 1].append(a[col - 1].pop(0))
        
    else:
        for j in range(distance):
            a[col - 1].insert(0, a[col - 1].pop())

res = 0
start = 0
end = n

for i in range(n):  
    for j in range(start, end):
        res += a[i][j]
        
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(res)
