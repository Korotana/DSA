def minJumps(self, arr):
    # code here

    size = len(arr)
    if size <= 1:
        return 0

    if arr[0] == 0:
        return -1

    jumps = 0
    cur_max = 0
    farthest = 0

    for i in range(size - 1):
        farthest = max(farthest, i + arr[i])

        if i == cur_max:
            jumps += 1
            cur_max = farthest
        if cur_max >= size - 1:
            return jumps

    return -1