# 소수(에라토스테네스 체)

import sys
sys.stdin =  open("./섹션 2/7. 소수(에라토스테네스 체)/in1.txt", "rt")

n = int(input())
ch =[0]*(n+1)  #인덱스번호가 20까지 생겨야 하니까 n+1 해준다
cnt = 0
# print(ch) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2,n+1):
    if ch[i] == 0:       #체크가 안되어 있으면  
        cnt += 1         #cnt 1로 체크
        for j in range(i,n+1,i):  # i가 2라면 2씩 증가하면서 2의 배수
            ch[j] = 1             # i가 3이라면 3씩 증가하면서 3의 배수 체크
        
print(cnt)
