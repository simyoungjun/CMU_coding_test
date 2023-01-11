#%% 2018 KAKAO BLIND RECRUITMENT / [1차] 캐시 / 2

def solution(cacheSize, cities):
    q = []
    time = 0
    for city in cities:
        city = city.lower()
        try: 
            i = q.index(city)
            q.pop(i)
            q.append(city)
            time += 1
        except:
            q.append(city)
            if len(q) > cacheSize:
                q.pop(0)
            time += 5
    return time

solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

#%% 행렬의 곱셈 / 2
def dot(a,b):
    s = 0
    for _1, _2 in zip(a, b):
        s += _1 * _2
    return s


def solution(arr1, arr2):
    out_shape = [len(arr1), len(arr2[0])]
    answer = [[] for j in range(out_shape[0])]
    
    arr2_new = []
    for j in range(out_shape[1]):
        arr2_new.append([arr2[i][j] for i in range(len(arr2))])
    
    for i in range(out_shape[0]):
        for j in range(out_shape[1]):
            answer[i].append(dot(arr1[i],arr2_new[j]))
    return answer

solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
# solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])

