def combine_word(s1, s2, default_ch):
    result = ""

    if default_ch in s1[0] + s2[0]:
        if s1[0] == default_ch and s2[0] == default_ch:
            result += default_ch
        else:
            if s1[0] != default_ch:
                result += s1[0]
            else:
                result += s2[0]
                
    if default_ch in s1[1] + s2[1]:
        if s1[1] == default_ch and s2[1] == default_ch:
            result += default_ch
        else:
            if s1[1] != default_ch:
                result += s1[1]
            else:
                result += s2[1]
                
    if default_ch in s1[2] + s2[2]:
        if s1[2] == default_ch and s2[2] == default_ch:
            result += default_ch
        else:
            if s1[2] != default_ch:
                result += s1[2]
            else:
                result += s2[2]
                
    if default_ch in s1[3] + s2[3]:
        if s1[3] == default_ch and s2[3] == default_ch:
            result += default_ch
        else:
            if s1[3] != default_ch:
                result += s1[3]
            else:
                result += s2[3]
                
    if default_ch in s1[4] + s2[4]:
        if s1[4] == default_ch and s2[4] == default_ch:
            result += default_ch
        else:
            if s1[4] != default_ch:
                result += s1[4]
            else:
                result += s2[4]
    return result
