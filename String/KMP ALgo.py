def search(self, pat, txt):
    # code here
    n, m = len(txt), len(pat)
    if m == 0:
        return []

    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    res = []
    i = j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                res.append(i - m)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return res