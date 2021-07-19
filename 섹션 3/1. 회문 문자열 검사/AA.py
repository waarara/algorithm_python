# 회문 문자열 검사

import sys
sys.stdin = open("./섹션 3/1. 회문 문자열 검사/in4.txt", "r")

# # 내가 푼것
# n = int(input())
# for i in range(n):
#     tmp = input()
#     tmp = tmp.lower()
#     if tmp == tmp[::-1]:
#         print(f"#{i+1} YES")
#     else:
#         print(f"#{i+1} NO")

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()    #s.lower()로 소문자로 할수도 있다
    size = len(s)     # 문자열의 길이를 구한다
    
    for j in range(size//2):
        if s[j] != s[-1-j]:      #인덱스 뒤에서 접근 [-1]
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))