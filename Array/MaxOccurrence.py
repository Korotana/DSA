def maxCountElement(arr):

    cur_max_element = arr[0]
    cur_max_count = 0

    for num in arr:
        if cur_max_count == 0:
            cur_max_element = num
            cur_max_count += 1
        elif cur_max_element == num:
            cur_max_count += 1
        else:
            cur_max_count -= 1

    return {"Element": cur_max_element}

print(maxCountElement([3,3,4]))


# slight variation
#
#
#
# def majorityElement(self, arr):
#     # code here
#     cur_max_element = arr[0]
#     cur_max_count = 0
#
#     for num in arr:
#         if cur_max_count == 0:
#             cur_max_element = num
#             cur_max_count += 1
#         elif cur_max_element == num:
#             cur_max_count += 1
#         else:
#             cur_max_count -= 1
#
#     if arr.count(cur_max_element) > len(arr) / 2:
#         return cur_max_element
#     return -1