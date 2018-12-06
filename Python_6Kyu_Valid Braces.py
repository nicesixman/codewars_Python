def validBraces(string):
    new_list = []
    for str_length in range(0, len(string)):
        if string[str_length] == '(':
            new_list.append('(')
            print(new_list)
            continue
        elif string[str_length] == '{':
            new_list.append('{')
            print(new_list)
            continue
        elif string[str_length] == '[':
            new_list.append('[')
            print(new_list)
            continue
        elif string[str_length-1] == '(' and string[str_length] == ')':
            new_list.pop()
            print(new_list)
            continue
        elif string[str_length-1] == '{' and string[str_length] == '}':
            new_list.pop()
            print(new_list)
            continue
        elif string[str_length-1] == '[' and string[str_length] == ']':
            new_list.pop()
            print(new_list)
            continue
        else:
            return False
    return True


validBraces('(({{[[]]}}))')
