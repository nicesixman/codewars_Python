def compare(s1, s2):
    s1sum = 0
    s2sum = 0
    if s1 is None:
        s1sum = 0
    else:
        for chrsearch in range(0, len(s1)):
            if s1[chrsearch].isalpha() == 0:
                s1sum = 0
                break
            elif s1[chrsearch].isupper() == 1:
                s1sum += (int(ord(s1[chrsearch])))
            elif s1[chrsearch].isupper() == 0:
                s1sum += (int(ord(s1[chrsearch])))-32
    if s2 is None:
        s2sum = 0
    else:
        for chrsearch in range(0, len(s2)):
            if s2[chrsearch].isalpha() == 0:
                s2sum = 0
                break
            elif s2[chrsearch].isupper() == 1:
                s2sum += (int(ord(s2[chrsearch])))
            elif s2[chrsearch].isupper() == 0:
                s2sum += (int(ord(s2[chrsearch])))-32
    if s1sum == s2sum:
        return 1
    else:
        return 0


compare("Sample", "Test")
