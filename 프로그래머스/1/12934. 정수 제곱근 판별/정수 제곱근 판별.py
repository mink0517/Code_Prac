def solution(n):
    answer = n ** (1/2)
    if answer % 1 == 0:
        answer = (answer + 1) ** 2
    else:
        answer = -1
    return answer