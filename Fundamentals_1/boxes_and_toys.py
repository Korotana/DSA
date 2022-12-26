toys_and_boxes = [input() for i in range(int(input()))]

def get_boxes_count(toys_and_boxes):
    correct_boxes = 0
    for box in toys_and_boxes:
        box = box.split(" ")
        num_toys = int(box[0])
        box_capacity = int(box[1])
        if (box_capacity - num_toys) > 1:
            correct_boxes += 1
    return correct_boxes

print(get_boxes_count(toys_and_boxes))

