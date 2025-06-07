
def maxSubArraySum(self, arr):
    # Your code here

    best = current = arr[0]

    for num in arr[1:]:
        current = max(num, num + current)
        best = max(best, current)

    return best