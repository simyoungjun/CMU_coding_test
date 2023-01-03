#%% 로그인 성공?
def solution(id_pw, db):
    answer = 'fail'
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'
#%% 시저 암호
def solution(s, n):
    C = []
    C_ = []
    for i in range(97,123):
        C_.append(chr(i))
    for i in range(65, 91):
        C.append(chr(i))
        
    answer = []
    for i in s:
        i_a = ord(i)
        if i == ' ':
            answer.append(i)
        elif i_a < 91:
            answer.append(C[(i_a - 65 + n)%26])
        else:
            answer.append(C_[(i_a - 97 + n)%26])
    return ''.join(answer)

solution('AB',1)