#%% 직사각형 넓이 구하기
import numpy as np
def distance(x1, x2):
    return np.sqrt(np.sum(np.abs(x1 - x2)**2))

def solution(dots):
    dots = np.array(dots)
    m_i = 0
    m_d = 0 
    for i in range(1, len(dots)):
        d_i = distance(dots[0], dots[i])
        if m_d < d_i:
            m_i = i
            m_d = d_i
        
    dots = np.delete(dots, m_i, axis = 0)
    return distance(dots[0], dots[1]) * distance(dots[0], dots[2]) 

solution([[1, 1], [2, 1], [2, 2], [1, 2]])
# % 두 수의 합
def solution(num1, num2):
    return num1 + num2