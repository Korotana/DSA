def maxCountElement(arr):

    cur_max_element = arr[0]
    cur_max_count = 0

    for num in arr:
        if cur_max_count == 0:
            cur_max_element = num
            cur_max_count += 1
        else:
            cur_max_count -= 1

    return {"Element": cur_max_element}

print(maxCountElement([0,0,1,2,2,0,1,2,2,1,1,1]))