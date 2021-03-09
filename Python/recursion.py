'''
# list A에 있는 가장 큰 수를 찾는 재귀함수

def find_max(A, n): # A[0] ~ A[n-1] 중 최대값을 찾아 리턴
    for A[n] in range(0, n):
        if A[n] < A[n+1]: # i = A[0], A[1] ... A[n-1]
            return A[n] 
        else: return find_max(A, n-1) 

A = [1, 5, 3, 4, 10, 8]

find_max(A, 6)
'''

# 재귀함수 : 함수(알고리즘) 내부에서 한 번 이상 자신의 함수(알고리즘)를 호출! 
'''
<재귀함수>
1) n == 1 테스트 : 바닥조건(basecase) → T(1) = 1 or C(상수시간)
2) 재귀호출 : T(n) = 점화식
=> 이 둘을 전개하여 T(n)에 관한 점화식을 만들고 그것을 O()로 단순화!
'''

# ex1) sum(n) = 1 + 2 + .... + (n-1) + n = sum(n-1) + n

def sum(n):
    if n == 1: return 1
    return sum(n-1) + n

# ex2) sum(a, b) = a + (a + 1) + ... + (b - 1) + b  (단, a<=b)

def sum2(a, b):
    if a == b: return a
    if a > b: return 0
    m = (a + b) // 2
    return sum2(a, m) + sum2(m+1, b)

print(sum(9))
print(sum2(1,9))