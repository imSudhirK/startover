# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

def isValidParentheses(s):
    open_brackets = {'(': 1, '{': 2, '[': 3}
    closed_brackets = {')': 1, '}': 2, ']': 3}
    stk = []
    for c in s:
        if c not in open_brackets and c not in closed_brackets:
            continue
        elif c in open_brackets:
            stk.append(open_brackets[c])
        elif stk and stk[-1] == closed_brackets[c]:
            stk.pop()
        else:
            return False
    return False if stk else True

print(isValidParentheses("(asda(sdf)[asfdsf]'{'asff'}'"))

        