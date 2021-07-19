# 두 리스트 합치기
import sys
sys.stdin = open("./섹션 3/4. 두 리스트 합치기/in1.txt", "r")

# # sort()를 써서 이렇게 하면 시간 복잡도가 n log n번이 되서 느림
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# c = a+b
# # c = set(c) ## 중복제거 안함
# c = list(c)
# c.sort()
# for i in c:
#     print(i)



# n번만에 하는 방법
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0   # 두지점을 가리키는 두 변수와
c = []        # 빈 리스트가 필요

while p1 < n and p2 <m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1

    else:
        c.append(b[p2])
        p2 += 1
    
if p1 < n:
    c = c+a[p1:]
if p2 < m:
    c = c+b[p2: ]   

for i in c:
    print(i, end=' ')