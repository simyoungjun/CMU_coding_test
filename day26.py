#%% 저주의 숫자3
def solution(n):
    i = 1
    answer = []
    count = 0
    while count < n:
        if i % 3 == 0 or '3' in str(i):
            pass
        else:
            answer.append(i)
            count += 1
        i += 1
    return answer[-1]

solution(15)

#%% 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(i + 1, l):
            s = numbers[i] + numbers[j]
            if s in answer:
                continue
            answer.append(s)

    return sorted(answer)