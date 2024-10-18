def compute_lps(pattern, m, lps):
    l = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1

    #return lps

def KMP_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = [0] * m

    compute_lps(pattern, m, lps)

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1
