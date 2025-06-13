def commonSubseq(a, b):
    set_a = set(a)
    set_b = set(b)

    # Check if the sets intersect
    if set_a & set_b:
        return 1
    else:
        return 0

print(commonSubseq("ABEF", "CADE"))  # Expected: 1 ("A", "E")
print(commonSubseq("ABCD", "EFGH"))  # Expected: 0
print(commonSubseq("abc", "xyz"))  # Expected: 0
print(commonSubseq("hello", "world"))  # Expected: 1 ("o", "l")
