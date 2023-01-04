#%% 저주의 숫자3
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        t = '3' in str(i)
        if i // 3 == 0:
            answer += 1
        else:
            answer += 1
    return answer

solution(10)