def solution(x):
    arr = []
    summ = 0
    for i in str(x):
        arr.append(i)
    for j in range(len(arr)):
        summ += int(arr[j])
    if x % summ == 0:
        answer = True
    else :
        answer = False
    return answer

print (solution(13))

