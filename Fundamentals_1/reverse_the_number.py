# TODO {https://mycode.prepbytes.com/problems/fundamentals/RVSREUM}

def reverse_the_number(number):
    endvalue = 0
    frontindex = 1

    if len(number) == 1:
        return number
    elif len(number) == 2:
        number = [*number]
        endvalue = number[-frontindex]
        number[-frontindex] = number[frontindex - 1]
        number[frontindex - 1] = endvalue
        number = "".join(number)
        return number
    else:
        number = [*number]
        mid = len(number) / 2
        if len(number) % 2 == 1:
            mid += 1

        while frontindex < mid:
            if len(number) % 2 == 0 and mid - frontindex == 1:
                endvalue = number[-frontindex-1]
                number[-frontindex-1] = number[frontindex]
                number[frontindex] = endvalue
            if len(number) % 2 == 1 and mid-frontindex == 1:
                continue
            endvalue = number[-frontindex]
            number[-frontindex] = number[frontindex - 1]
            number[frontindex-1] = endvalue
            frontindex += 1
        number = "".join(number)
        return number

print(reverse_the_number(input()))

# TODO Another approach would be using split on string
