# 점수 계산

import sys
sys.stdin = open("./섹션 2/10. 점수 계산/in5.txt", "r")

n = int(input())
score =list(map(int, input().split()))
# print(n)
# print(score)

sum = 0
cnt = 0

for x in score:
    if x==1:            #연속해서 1이 나오면 1점씩 증가되서 누적되게
        cnt +=1         #4번 연속 정답이라면 cnt는 1씩 증가해 4가 되고
        sum += cnt      #sum엔 1+2+3+4 점수가 누적된다 
    else:
        cnt=0           #오답일 경우 0으로 초기화

print(sum)