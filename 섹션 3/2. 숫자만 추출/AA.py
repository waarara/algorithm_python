# 숫자만 추출

import sys
sys.stdin = open("./섹션 3/2. 숫자만 추출/in1.txt", "r")

s = input()
print(s)
res = 0

for x in s:
    # print(x, end=' ')
    if x.isdecimal():
        res = res*10 + int(x)
print(res)

cnt = 0

for i in range(1,res+1):
    if res % i ==0:
        cnt += 1
print(cnt)
