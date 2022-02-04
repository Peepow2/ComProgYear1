def combine_word(s1, s2, default_ch):
    result = ""
    for i in range(5):
        if default_ch in s1[i] + s2[i]:
            if s1[i] == default_ch and s2[i] == default_ch:
                result += default_ch
            else:
                if s1[i] != default_ch:
                    result += s1[i]
                else:
                    result += s2[i]
    return result
