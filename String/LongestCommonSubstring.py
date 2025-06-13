def longestCommonSubstr(s1, s2):
    n = len(s1)
    m = len(s2)

    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                max_len = max(max_len, curr[j])
            else:
                curr[j] = 0
        prev, curr = curr, [0] * (m + 1)

    return max_len


# Test case 1
print(longestCommonSubstr("ABCDGH", "ACDGHR"))  # Expected: 4 ("CDGH")

# Test case 2
print(longestCommonSubstr("abc", "acb"))        # Expected: 1 ("a", "b", or "c")

# Test case 3
print(longestCommonSubstr("YZ", "yz"))          # Expected: 0 (case-sensitive!)

# Test case 4
print(longestCommonSubstr("abcdef", "zabcf"))   # Expected: 3 ("abc")

# Test case 5
print(longestCommonSubstr("abcxyz123", "xyz123abc"))  # Expected: 6 ("xyz123")

