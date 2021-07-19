import sys
sys.stdin = open("./섹션 3/5. 수들의 합/in1.txt", "r")

n,m = map(int, input().split())
# print(n,m)
a = list(map(int,input().split()))
# print(a)

lt = 0
rt = 1
tot = a[0]
cnt =0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
        

print(cnt)