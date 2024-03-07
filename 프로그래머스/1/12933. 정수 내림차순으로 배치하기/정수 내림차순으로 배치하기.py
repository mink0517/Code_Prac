def solution(n):
    answer = list(str(n))
    
    answer.sort(reverse = True) # 내림차순
    
    result = int(''.join(answer))
    
    return result