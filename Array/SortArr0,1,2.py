# Function to sort an array of 0s, 1s, and 2s
def sort012(arr):
    # code here
    # code here

    current = 0
    twos = len(arr) - 1
    zeros = 0

    while current <= twos:
        if arr[current] == 0:
            arr[zeros], arr[current] = arr[current], arr[zeros]
            current += 1
            zeros += 1
        elif arr[current] == 1:
            current += 1
        elif arr[current] == 2:
            arr[twos], arr[current] = arr[current], arr[twos]
            twos -= 1

    return arr


a = [0,1,2,0,1,2]

print(sort012(a))