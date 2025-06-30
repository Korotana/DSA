def missingNum(arr):
    # code here
    arr_sum = sum(arr)
    total_sum = sum(range(1, len(arr)+2))
    return total_sum - arr_sum
arr = [1, 2, 3, 5]

print(missingNum(arr))

