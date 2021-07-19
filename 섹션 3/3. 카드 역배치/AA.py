import sys
sys.stdin = open("./섹션 3/3. 카드 역배치/in1.txt", "r")

a = list(range(21))
for i in a:
    print(i, end=' ')
print()   #출력 --> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

for _ in range(10):
    s,e = map(int, input().split())
    for i in range((e-s+1)//2):
       a[s+i], a[e-i] = a[e-i],a[s+i]

a.pop(0)
for i in a:
    print(i, end=' ')
print()  #출력 --> 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

# 문제의 핵심은 스와프
# a = 10
# b = 'abc'
# a,b = b,a
# 다른 언어라면
# a = 3
# b = 'abc'
# tmp = a
# a = b
# b = tmp