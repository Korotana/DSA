def minRepeats(A,B):
    repeated = A
    count = 1

    while len(repeated) < len(B):
        repeated += A
        count += 1

    if B in repeated:
        return count

    repeated += A
    count += 1

    if B in repeated:
        return count

    return -1

A = "abcd"
B = "cdabcdab"
minRepeats(A,B)

A = "ab"
B = "cab"
minRepeats(A,B) #---> -1 No matter how many times we repeat A, we can't get a string such that B is a substring of it.





