def findIndex(str):
    # Your code goes here
    length = len(str)
    close_total = str.count(")")
    open = 0

    for brac in range(length):
        if open == close_total:
           return brac
        if str[brac] == "(":
            open += 1
        else:
            close_total -= 1
    return length


print(findIndex("(())))("))  # Output: 4
print(findIndex("))"))      # Output: 2
print(findIndex("(((())))"))# Output: 4
print(findIndex(""))