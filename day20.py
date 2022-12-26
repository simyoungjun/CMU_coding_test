#%% 올바른 괄호
def solution(s):
    answer = True
    a = []
    
    for i in range(len(s)):
        if s[i] == '(':
            a.append(s[i])
        
        elif len(a) != 0 and s[i] == ')':
            a.pop()
        else:
            return False
                
    if len(a) != 0:
        
        answer = False

    return answer
#%%
def solution(n, m):
    answer = []
    
    for i in range(min(m,n), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    
    for i in range(max(n,m), (n*m) + 1):
        if i % m == 0 and i % n == 0:
            answer.append(i)
            break

    return answer
