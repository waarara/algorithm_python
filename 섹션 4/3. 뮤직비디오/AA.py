import sys
sys.stdin = open("./섹션 4/3. 뮤직비디오/in1.txt", "r")

def count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n,m = map(int, input().split())
music = list(map(int, input().split()))
maxx = max(music)
# print(n,m)
# print(music)

lt = 1
rt = sum(music)
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if mid >= maxx and count(mid) <= m:
        
        res = mid
        rt = mid-1
    else:
        lt = mid + 1

print(res)

