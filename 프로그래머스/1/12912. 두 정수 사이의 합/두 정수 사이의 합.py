def solution(a, b):
    answer = 0
    
    if a > b:
        mi = b
        ma = a
    else:
        mi = a
        ma = b
    for i in range(mi, ma+1):
        answer += i
    return answer