def solution(text, ending):
    # your code here...
    return True if text[-2:] == ending[-2:] else False
    pass


print(solution('ails', 'fails'))
