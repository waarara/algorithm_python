# 스도쿠 검사
import sys
sys.stdin = open("./섹션 3/10. 스도쿠 검사/in1.txt", "r")

def check(a):
    for i in range(10):
        ch_row = [0]*10
        ch_cul = [0]*10
        for j in range(10):
            ch_row[a[i][j]] = 1
            ch_cul[a[j][i]] = 1
            if sum(ch_row) !=9 or sum(ch_cul)!=9:
                return False
    for i in range(3):
        for j in range(3):
            ch_3x3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch_3x3[a[i*3+k][j*3+s]] = 1
            if sum(ch_3x3) !=9:
                return False
    return True



a = [list(map(int,input().split())) for _ in range(9)]

if check(a):
    print('YES')
else:
    print('NO')