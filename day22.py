#%% 치킨 쿠폰
def solution(chicken):
    answer = 0
    for i in range(8):
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10
        
    return answer

solution(1000000)

#%% 문자열 밀기
def solution(A, B):
    
    if A == B:
        return 0
    
    L = len(A)
    A = list('0'*L + A)
    
    for i in range(L):
        A[L-1 - i] = A[-1 - i]
        A[-1 - i] = '0'
        S = ''.join(A)
        if B in S:
            return i + 1
    return -1

solution("apple","elppa")