from array import array
d = 9
arr = array('i', [7,3,9,1])   # 'i' = signed 32-bit int

d %= len(arr)
print(d)


def rotateArr(self, arr, d):
    # Your code here
    size = len(arr)
    d %= len(arr)
    if d == 0:
        return


    def revers(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    revers(0, d - 1)
    revers(d, size - 1)
    revers(0, size - 1)


# for index in range(d):
#     element = arr[0]
#     arr.remove(arr[0])
#     arr.insert(len(arr), element)

