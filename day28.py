#%% 점프와 순간이동 / Summer/Winter Coding(~2018) / 2
def solution(n):
    d = {0 : 0, 1 : 1}
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            d[i] = d[i//2]
        else:
            d[i] = d[(i - 1) // 2] + 1
        
        
    return d[n]

solution(5000)

#%% 점프와 순간이동 / Summer/Winter Coding(~2018) / 2
def solution(n):
    answer = 1
    while(n != 1):
        if n % 2 == 0:
            n = n//2
        else:
            n = (n - 1)//2
            answer += 1
    return answer

solution(5000)

#%% 멀리뛰기 / 연습문제 / 2
def solution(n):
    answer = 0
    c = {0 : 1, 1 : 1}
    for i in range(2, n + 1):
        c[i] = c[i -1] + c[i - 2]
        print(i, c[i])
    return c[n] % 1234567

solution(10)
