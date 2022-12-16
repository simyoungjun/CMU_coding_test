#%% 숫자 문자열과 영단어
def solution(s):
    pron = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(pron)):
        s = s.replace(pron[i],str(i))
    print(s)
    
    answer = int(s)
    return answer

#%% k번째 수
def solution(array, commands):
    answer = []
    for com in commands:
        com_arr = array[com[0]-1:com[1]]
        com_arr.sort()
        answer.append(com_arr[com[2]-1])
    return answer