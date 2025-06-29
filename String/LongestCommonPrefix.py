def longestCommonPrefix(arr):
    if not arr:
        return ""

    prefix = arr[0]

    for string in arr[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

print(longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]))
