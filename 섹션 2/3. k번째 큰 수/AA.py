# k번째 큰 수
import sys
sys.stdin = open("./섹션 2/3. k번째 큰 수/input.txt", "rt")

n,k = map(int,input().split())
a = list(map(int, input().split()))
print(n,k)
print(a)

result = set()  #set() 중복값을 제거해주는 함수 집합
# (),[],{} 튜플, 리스트,딕셔너리 차이점 기억

for i in range(n):   #3장의 카드를 뽑는 모든 경우의 수이기 때문에 3중 for문을 돌린다
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(a[i]+a[j]+a[m]) #리스트의 .append와 달리 딕셔너리는 .add

# print(result) 하면 딕셔너리 형태로 출력된다
result = list(result)   #리스트로 형변환
# print(result)
result.sort(reverse=True) # 내림차순으로 정렬
print(result[k-1])        # 0번 인덱스 부터 시작이기 때문에  -1을 해준다
          