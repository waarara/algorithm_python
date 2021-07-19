# import sys
# sys.stdin = open("./섹션 4/1. 이분검색/input.txt", "r")

# n,m = map(int, input().split())
# # print(n,m)
# a = list(map(int, input().split()))

# a.sort()
# lt = 0
# rt = n-1  # 0번부터7번 인덱스 까지이므로 n=8이기때문에 
#           # 인덱스 범위를 벗어나기 때문에 -1을 해준다


# while lt <= rt:
#     mid = (lt+rt)//2
#     if a[mid] == m:
#         print(a[mid])
#         print(mid+1)  #인덱스 0번 부터 시작이라 +1을 해준다
#         break

#     elif a[mid] > m:
#         rt = mid-1
    
#     else:
#         lt = mid + 1

import sys
sys.stdin = open("./섹션 4/1. 이분검색/in1.txt", "r")
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n-1
mid = 0

while lt <= rt:
    mid = (lt+rt)//2

    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid -1
    else:
        lt = mid +1