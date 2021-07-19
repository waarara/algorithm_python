import sys
sys.stdin = open("./섹션 4/4. 마구간 정하기/in3.txt", "r")

def count(len):
    cnt = 1
    ep = line[0] #end point
    for i in range(1,n):
        if line[i]-ep >= len:
            cnt += 1
            ep = line[i]
    return cnt


n,c = map(int, input().split())
# print(n,c)

line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()

# print(line)
lt = 1
rt = line[n-1]

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)