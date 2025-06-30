def multiplyStrings(s1, s2):
    neg = False
    if s1[0] == '-':
        neg = not neg
        s1 = s1[1:]
    if s2[0] == '-':
        neg = not neg
        s2 = s2[1:]

    # Edge case: if one is zero
    if s1 == "0" or s2 == "0":
        return "0"

    n, m = len(s1), len(s2)
    result = [0] * (n + m)

    # Multiply each digit from end
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1

            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10

    # Skip leading zeros
    res = []
    for digit in result:
        if not (len(res) == 0 and digit == 0):
            res.append(str(digit))

    product = ''.join(res)
    return '-' + product if neg else product


multiplyStrings("0033","2")


    
--------------------pseudocode--------------------

