#%% N개의 최소공배수
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a, b))
    return arr[0]

solution([2,6,8,14])
#%% 예상 대진표
def solution(n,a,b):
    count = 0
    while b != a:
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        count += 1
    return count

solution(8, 4, 7)