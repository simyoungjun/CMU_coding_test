#%% 삼총사
n = [-3, -2, -1, 0, 1, 2, 3]
num_len = len(number)
_ = 0
for i in range(num_len):
    for j in range(i+1,num_len):
        for k in range(j+1,num_len):
            if sum([n[i],n[j],n[k]]) == 0:
                print([i,j,k])
                _ += 1


#%% 짝지어 제거하기
s = 'a'*100000000
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    if not(answer):
        return 1
    else:
        return 0

solution(s)
#%%

