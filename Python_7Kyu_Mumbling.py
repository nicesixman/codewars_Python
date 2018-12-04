def accum(s):
    result_list = []
    for a in range(0, len(s)):
        result = (str(s[a])).upper() + str((s[a]).lower())*a
        result_list.append(result)
        result_list.append("-")
    result_list.pop()
    return ''.join(result_list)


accum("SampleTest")
