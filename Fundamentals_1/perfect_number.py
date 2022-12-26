# https://mycode.prepbytes.com/problems/fundamentals/PRFCTNO

numbers = [input() for i in range(int(input()))]

def check_perfect(number):
    sum = 0

    for digit in range(1, number):
        if number % digit == 0:
            sum = sum + digit

    if sum == number:
        return "true"
    return "false"

for number in numbers:
    print(check_perfect(int(number)))
