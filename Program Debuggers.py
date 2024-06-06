def solution(text, end):
    return True if text[-len(end):] == end else False


print(solution('ails', 'fails'))
