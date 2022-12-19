#%% 가장 큰 수 x

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    

#%% 구명보트 ox
people = [70, 80, 50]
limit = 100
num = 0

people.sort()
a = 0
b = len(people) - 1
while a > b:
    if people[a] + people[b] >= limit:
        a += 1
        num +=1
    b -= 1
    
    
print( len(people)- num)

#%% 구명보트
def solution(people, limit):
    num = 0

    people.sort()
    print(people)
    for i in range(len(people)):
        two = False
        if people[i] > 240:
                continue
        for j in range(len(people) - 1, i, -1):
            if people[i] + people[j] <= limit:
                people[i], people[j] = 250, 250
                num += 1
                break
    return len(people) - num