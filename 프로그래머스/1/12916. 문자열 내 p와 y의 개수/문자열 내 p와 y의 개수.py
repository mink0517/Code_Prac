def solution(s):
    answer = True

    s = s.lower()
    ynum = s.count('y')
    pnum = s.count('p')
    
    if pnum == ynum:
        answer = True
    else:
        answer = False

    return answer