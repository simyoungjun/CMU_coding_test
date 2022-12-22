#%% 유한소수 판별하기 (x)
def solution(a, b):
    go = True
    if a/b == a//b:
        return 1
    elif b/a == b//a:
        b = b//a
    else:
        b = b
        
    while go:
        if b == 1:
            return 1
        if b/2 == b//2:
            b = b//2
            continue
        elif b/5 == b//5:
            b = b//5
            continue
        
        else:
            return 2

solution(1,512)
#%% 답
from math import gcd

def solution(a, b):
    go = True
    b = b// gcd(a,b)
        
    while go:
        if b == 1:
            return 1
        if b/2 == b//2:
            b = b//2
            continue
        elif b/5 == b//5:
            b = b//5
            continue
        
        else:
            return 2

solution(1,512)

#%% 등수 매기기 (o)


def solution(score):
    answer = []
    mean_score = []
    for s in score:
        mean_score.append(sum(s)/2)
    
    num = 1
    while num <= len(mean_score):
        max_ = [[mean_score[0], 0]]
        for j in range(1, len(mean_score)):
            print(max_[0][0], mean_score[j])
            
            if max_[0][0] < mean_score[j]:
                max_ = [[mean_score[j],j]]
            elif max_[0][0] == mean_score[j]:
                max_.append([mean_score[j],j])
                
        for k, i in enumerate(max_):
            
            mean_score[i[1]] = -1
            score[i[1]] = num
            
        num += k+1
    return score

solution([[0, 0], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])