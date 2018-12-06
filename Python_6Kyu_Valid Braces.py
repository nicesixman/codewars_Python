def validBraces(string):
    new_list = []
    if string[0] == ')' or string[0] == '}' or string[0] == ']':
        return False
    for str_length in range(0, len(string)):
        if string[str_length] == '(':
            new_list.append('(')
            stack = 1
            # print(new_list)
        elif string[str_length] == '{':
            new_list.append('{')
            stack = 1
            # print(new_list)
        elif string[str_length] == '[':
            new_list.append('[')
            stack = 1
            # print(new_list)
        elif string[str_length] == ')' and string[str_length - stack] == '(':
            new_list.pop()
            stack += 2
            # print(new_list)
            # print(stack)
        elif string[str_length] == '}' and string[str_length - stack] == '{':
            new_list.pop()
            stack += 2
            # print(new_list)
            # print(stack)
        elif string[str_length] == ']' and string[str_length - stack] == '[':
            new_list.pop()
            stack += 2
            # print(new_list)
            # print(stack)
        else:
            return False
    if new_list:
        return False
    return True


validBraces('([{}])')
