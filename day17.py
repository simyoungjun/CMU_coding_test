# 정수 제곱근 판별
def solution(n):
    answer = -1
    for i in range(int(n**0.5)+1):
        if i**2 == n:
            answer = (i+1)**2
            
    return answer

#%% 문자열을 정수로 바꾸기

def solution(s):
    answer = int(s)
    return answer