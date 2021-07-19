# 자릿수의 합

n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:        # 125라면
        sum += x%10     # 125를 10으로 나눈 나머지는 5
        x=x//10         # 몫은 12, 또 돌면 12를 나눈 나머지는 2 몫은 1
                        # 나머지는 1이므로 sum에 +=1 해주고 몫은 0이되니 break
    return sum    

# # 파이썬 스트링으로 처리하는 방법
# def digit_sum(x):
#     sum = 0
#     for i in str(x):   #str()로 스트링 형태로 변환
#         sum += int(i)  #125라면int로 형변환해 +=1, +=2, +=5 해서 하나씩 구하는 방법 
#     return sum
    
max = -2147000000
for x in a:   # a 리스트의 원소 하나씩 접근 
    # print(x)
    total = digit_sum(x)
    if total > max:
        max = total
        result = x
        
    
print(result)