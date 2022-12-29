#%% [1차] 비밀지도 > 2018 KAKAO BLIND RECRUITMENT
def solution(n, arr1, arr2):
    a, b = [], []
    for i in arr1:
        s = bin(i)[2:]
        if len(s) != n:
            a.append('0'*(n - len(s)) + s)
        else:
            a.append(s)
    for i in arr2:
        s = bin(i)[2:]
        if len(s) != n:
            b.append('0'*(n - len(s)) + s)
        else:
            b.append(s)     
             
    a = list(map(list,a))
    b = list(map(list,b))
    answer = a.copy()
    for i in range(n):
        for j in range(n):
            if int(a[i][j]) == 0 and int(b[i][j]) == 0:
                answer[i][j] = ' '
            else:
                answer[i][j] = '#'
                

    print(''.join(answer[i]))
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

#%% 최소직사각형 > 완전탐색
def solution(sizes):
    for size in sizes:
        if size[0] <size[1]:
            size[0], size[1] = size[1], size[0]
    max_0 = 0
    max_1 = 0
    for i, size in enumerate(sizes):
        if size[0] > max_0:
            max_0 = size[0]
        if size[1] > max_1:
            max_1 = size[1]
        
    print(sizes)
    answer = max_0*max_1
    return answer

solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])

# %
