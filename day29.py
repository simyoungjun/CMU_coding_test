#%% 다항식 더하기 / 0

def solution(polynomial):
    x_num, num = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric():
            num += int(i)
        else:
            if len(i) == 1:
                x_num += 1
            else:
                x_num += int(i[:-1])
    
    x_num, num = str(x_num), str(num)
       
    if x_num == "0" and num == "0":
        return "0"
    if x_num == "0":
        return num
    if x_num == "1":
        x_num = ""
    if num == "0":
        return x_num + "x"
    return x_num + "x + " + num

solution("x + 3x + 7 + x")

#%% 최빈값 구하기 / 0
def solution(array):
    answer = 0
    a = {}
    for i in array:
        try:
            a[i] += 1   
        except:
            a[i] = 1

    s_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    
    print(s_a)
    if len(s_a) == 1:
        return s_a[0][0]
    else:
        if s_a[0][1] == s_a[1][1]:
            return -1
        else:
            return s_a[0][0]

solution([0,1,1])