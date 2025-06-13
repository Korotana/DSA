def isRotated(self, s1, s2):
    if len(s1) != len(s2):
        return False

    n = len(s1)

    if n <= 2:
        return s1 == s2

    anti_clockwise_match = True
    for i in range(n):
        s1_index = (i + 2) % n
        if s1[s1_index] != s2[i]:
            anti_clockwise_match = False
            break

    if anti_clockwise_match:
        return True

    clockwise_match = True
    for i in range(n):
        s1_index = (i - 2 + n) % n
        if s1[s1_index] != s2[i]:
            clockwise_match = False
            break

    return clockwise_match