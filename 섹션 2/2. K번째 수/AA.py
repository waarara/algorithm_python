# k번째 수
# import os  ##현재 경로 확인
# currentpath = os.getcwd()
# print(currentpath)

import sys
sys.stdin = open("./섹션 2/2. K번째 수/in5.txt", "rt")
T = int(input())
print(T)

for t in range(T):
    n,s,e,k = map(int,input().split())
    a=list(map(int, input().split()))

    # print(a)

    tmp = a[s-1 : e]   


    tmp.sort()
    # print("#%d %d" %(t+1, tmp[k-1]))
    print(f"#{t+1}", tmp[k-1])   #f-스트링

# 리스트 슬라이싱 범위 잘 기억
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[2:5]) 
# [3,4,5] 가 출력된다 0번 인덱스 부터 시작이니 s는 -1을 해주고 
# e는 e 인덱스 이전까지 슬라이싱 된다
