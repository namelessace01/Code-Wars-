# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).

def solution(text, end):
    return True if text[-len(end):] == end else False


# Test Examples for the function
solution("samurai", "ai")
solution("ninja", "ja")
solution("sensei", "i")
solution ("abc", "abc")
solution("abcabc", "bc")
solution("fails", "ails")
solution("sumo", "omo")
solution("samurai", "ra")
solution("abc", "abcd")
solution("ails", "fails")
solution("this", "fails")
solution("spam", "eggs")