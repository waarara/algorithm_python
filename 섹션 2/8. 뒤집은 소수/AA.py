# 뒤집은 소수

import sys
sys.stdin = open("./섹션 2/8. 뒤집은 소수/input.txt", "r")


def reverse(x):
    res = 0
    while x>0:                                   #0보다 클때만 참 0이 되면 break
        t = x%10                                 #x의 1의 자리수가 t가 된다
        res = res*10+t
        x = x//10                      #x는 10으로 나눈 몫으로 바뀌고 다시 while문 돈다
    return res                         #while문이 break되면 res를 return

def isPrime(x):
    if x ==1:                           #1이 넘어오면 False 1은 제외 시키고 시작한다
        return False
    for i in range(2, x//2+1):    #2부터 돌면서 소수인지 확인 x//2로 나눈몫까지 돌려면 +1
                                       # 16이 들어온다면 16=1*16
                                       #                16=2*8 
        if x%i ==0:                       #x를 i로 나눠서 0이 된다면 약수가 
            return False                  #존재하는것이기 때문에소수가 될 수 없다
    else:
        return True


n = int(input())
a = list(map(int, input().split()))
# print(a) #[32, 55, 62, 3700, 250]
# print(reverse(123456789))  #reverse 함수 확인용 987654321 로 출력된다
# print(reverse(9010)) #109로 출력

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):                         #isPrime이 참이면
        print(tmp, end=' ')                  #tmp 출력


