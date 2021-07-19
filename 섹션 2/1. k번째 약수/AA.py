import sys
sys.stdin = open("./섹션 2/1. K번째 약수/in1.txt", "rt")

n,k = map(int, input().split())  #string 형태로 입력되기 때문에 int로 정수화 
                                #n,k를 공백을 두고 맵핑

cnt = 0

for i in range(1,n+1):    # n+1을 해줘야 그 숫자까지 돈다
    if n%i ==0:           # for문이 1부터 8까지 돌면서 n을 i로 나눈 나머지가
                          # 0이 되는것은 약수 이기 때문에 cnt 1증가시킨다
        cnt += 1
    if cnt == k:          # k번째 약수가 발견 됐으면 출력해준다
        print(i)
        break
else:
    print(-1)     #for - else 문으로 약수가 없으면 -1을 출력