

def split_pile(num,partition):
    parted = []
    for i in range(partition):
        if num < partition and i < num:
            parted.append(num//partition+1)
        else:
            if (num % partition) != 0 and i < 1:
                parted.append(num//partition+1)
            else:
                parted.append(num//partition)
    return parted



def partition_pile(starting_stack_size, max_stable_height, partition):
    queue = []
    max_split = starting_stack_size
    queue.append(max_split)
    partitioned = []
    queue_size = len(queue)
    while max_split > max_stable_height or queue_size != 0:
        dequeue = queue.pop(0)
        print(len(queue))
        parts = split_pile(dequeue,partition)
        max_split = max(parts)
        for i in parts:
            if i <= max_stable_height:
                partitioned.append(i)
            else:
                queue.append(i)
        queue_size = len(queue)
    return partitioned

Test Case partition_pile(13,3,2)
	Output: [3, 3, 3, 2, 2]
