# import sys
# sys.stdin = open("./섹션 4/2. 랜선자르기/in2.txt", "r")

# def count(len): 
#     cnt = 0
#     for x in line:
#         cnt += (x//len)
#     return cnt

# k,n = map(int, input().split())
# line = []
# res = 0
# largest = 0

# for i in range(k):
#     tmp = int(input())
#     line.append(tmp)
#     largest = max(largest, tmp)

# lt = 1
# rt = largest

# while lt <= rt:
#     mid = (lt+rt)//2
#     if count(mid) >= n:
#         res = mid
#         lt = mid+1
#     else:
#         rt = mid-1

# print(res)

# def count(len):
#     cnt = 0
#     for x in line:
#         cnt += (x//len)


n = 6
times = [7,10]

print(max(times)*n)









