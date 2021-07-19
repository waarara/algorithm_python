# 정다면체

import sys
sys.stdin =  open("./섹션 2/5. 정다면체/in1.txt", "rt")
n,m = map(int, input().split())
print(n,m)

cnt = [0]*(n+m+3)  #n=4 이고 m=6 일때 10 이상의 값은 나오진 않겠지만 넉넉하게 
                   # +3 해준것 일뿐 아무 의미 없음 +1만 해줘도된다
                   #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                   #13개의 0으로 초기화
max = 0

for i in range(1,n+1):  # 1부터4까지 돌기 위해서 n+1
    for j in range(1,m+1):
        cnt[i+j]+=1

print(cnt)         #[0, 0, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0, 0]으로 출력
                   # 5,6,7 번 인덱스가4번 증가해 가장 높게 나온다

for i in range(n+m+1): #n+m은 10인데 range를 10으로 잡으면 10 이전 9까지 돈다 그래서 +1
    if cnt[i]>max:  
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=" ")
    