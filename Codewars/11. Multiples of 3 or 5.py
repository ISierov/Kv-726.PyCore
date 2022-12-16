def solution(number):
    res = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res
