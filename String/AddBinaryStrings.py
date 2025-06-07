def addBinary(self, s1, s2):
    # code here
    i = 1
    carry = 0
    out = []
    while i <= len(s1) or i <= len(s2) or carry != 0:
        bit1 = int(s1[-i]) if i <= len(s1) else 0
        bit2 = int(s2[-i]) if i <= len(s2) else 0

        total = bit1 + bit2 + carry
        out.append(str(total % 2))
        carry = total // 2

        i += 1

    result = ''.join(reversed(out)).lstrip('0') or '0'

    return result