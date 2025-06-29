def removeDuplicates(s):
    bit_upper_case = 0
    bit_lower_case = 0
    result = []

    for char in s:
        oc = ord(char)
        if 65 <= oc <= 90:  # if 'A' <= char <= 'Z':
            bit = 1 << (oc - 65) # bit = 1 << (oc - ord('A'))
            if not (bit_upper_case & bit):
                bit_upper_case |= bit
                result.append(char)
        elif 97 <= oc <= 122:  # elif 'a' <= char <= 'z':
            bit = 1 << (oc - 97) # bit = 1 << (oc - ord('a'))
            if not (bit_lower_case & bit):
                bit_lower_case |= bit
                result.append(char)

    return ''.join(result)

print(removeDuplicates("geEksforGEeks"))  # Output: "geEksforG"
print(removeDuplicates("HaPpyNewYear"))   # Output: "HaPpyNewYr"
print(removeDuplicates("aAaAaA"))         # Output: "aA"
