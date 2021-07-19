# 주사위 게임

import sys
sys.stdin = open("./섹션 2/9. 주사위 게임/in5.txt", "r")

n = int(input())
res = 0

for i in range(n):
    tmp = input().split()    #int 인자를 안주고 input받으면 스트링 default
    tmp.sort()               #비교 용이하게 정렬
    # print(tmp)               #['1', '2', '3'] 스트링 형태로 리스트에 들어가 있다
    #     
    a,b,c = map(int, tmp)    #int형으로 변환하면서 a,b,c에 할당되게 map해준다  
    # print(a,b,c)             # 1,2,3 으로 출력
    
    if a==b and b==c:
        money = 10000 + a*1000
    elif a==b or a==c:
        money = 1000 + (a*100)
    elif b==a or b==c:
        money = 1000 + (b*100)
    else:
        money = c*100

    if money>res:
        res = money

print(res)