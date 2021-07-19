# 대표값
import sys
sys.stdin = open("./섹션 2/4. 대표값/input.txt", "rt")

n =int(input())
a = list(map(int, input().split()))

for i in range(len(a)): #range를 입력된 n개만큼을 해도되고 리스트 a의 길이만큼 해도된다
    print(a[i], end=" ")
print()

avg = round(sum(a)/n)  #round(3.1415,2) 두번째 인자로 소수점 자리수지정, 
                       #안쓰면 default로 소수점 첫자리에서 반올림  
# print(avg)

# int형의 최대값 2147000000
# int형의 최소값 -2147000000
# 또는 tmp = float('inf')로 무한대로 초기화

min = 2147000000  

for idx, x in enumerate(a):   #enumerate() 리스트의 인덱스와 값을 쌍으로 가져옴
    tmp=abs(avg-x)            #abs() 절대값 구하는 함수
    # print(idx+1, x, tmp)
    if tmp<min:             
        min = tmp
        score = x
        res = idx+1
    # 첫번째 과정 74-45=29  tmp=29가 되고 min보다 작으므로 min값을 tmp로 대체
    
    elif tmp==min:         #tmp 점수차가 같을 경우 
        if x > score:      #점수가 높은걸 답으로 대체 
            score = x
            res = idx+1

print(avg, res)

    