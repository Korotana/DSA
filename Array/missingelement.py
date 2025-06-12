
def missingNum(self, arr):
    # code here
    size = len(arr)
    total = sum(range(1,size+2))

    for num in arr:
        total -= num

    return total