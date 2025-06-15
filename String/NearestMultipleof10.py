def roundToNearest(s):
    # Complete the function
    num = int(s)

    remainder = num % 10
    quotient = num // 10
    print(remainder)
    if remainder > 5:
        return quotient * 10 + 10
    return quotient * 10

print(roundToNearest(15))

#Fails for very large input as we cannot covert them to small nums

