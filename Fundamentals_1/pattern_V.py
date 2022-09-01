Char = input()

def print_V():
    row_length = 10
    numbers_string_forward = ""
    numbers_string_backward = ""
    for char in range(1, 6):
        numbers = 2 * char
        spaces = row_length - numbers
        numbers_string_forward = numbers_string_forward + str(char)
        numbers_string_backward = str(char) + numbers_string_backward
        row_string = numbers_string_forward + " " * spaces + numbers_string_backward
        print(row_string)

print_V()
