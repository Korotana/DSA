def nonRepeatingChar(s):
    # code here

    from collections import Counter

    count = Counter(s)

    for char in s:
        if count[char] == 1:
            return char

    return '$'