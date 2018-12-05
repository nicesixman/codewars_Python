def validBraces(string):
    new_list = []
    for str_length in range(0, len(string)):
        if string[str_length] == '(':
            new_list.append(1)
            continue
        elif string[str_length] == ')':
            new_list.append(-1)
            continue
        elif string[str_length] == '{':
            new_list.append(2)
            continue
        elif string[str_length] == '}':
            new_list.append(-2)
            continue
        elif string[str_length] == '[':
            new_list.append(3)
            continue
        elif string[str_length] == ']':
            new_list.append(-3)
            continue
    print(new_list)
    if len(new_list) % 2 == 1:
        return False
    elif sum(new_list) != 0:
        return False
    else:
        print('need for algorithm')
        return 


validBraces('(){}[]')
