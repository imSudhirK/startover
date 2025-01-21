# Decode String
# https://leetcode.com/problems/decode-string

s = "2[abc]3[cd]ef"

curr_string = ''
stk = []
curr_number = 0

for c in s:
    if c.isalpha():
        curr_string += c
    elif c.isdigit():
        curr_number = curr_number * 10 + int(c)
    elif c == "[":
        stk.append(curr_string)
        stk.append(curr_number)
        curr_string = ''
        curr_number = 0
    elif c == "]":
        num = stk.pop()
        prev_string = stk.pop()
        curr_string = prev_string + num * curr_string
    else: continue

print("Decoded string: ", curr_string)

