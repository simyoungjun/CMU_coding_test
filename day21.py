#%% 특이한정렬 x
num_list = [1, 2, 3, 4, 5, 6]
n = 4



def solution(num_list, n):
    return sorted(num_list, key=lambda x: (abs(n-x), -x))
    

solution(num_list, n)

#%% 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer

solution(["abce", "abcd", "cdx"], 2)