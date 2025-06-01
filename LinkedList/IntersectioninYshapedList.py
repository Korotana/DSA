from LinkedList.Node import Node


class Solution:

    def get_length(head):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        return count

    def intersectPoint(self, head1, head2):
        # code here

        list1_len = Solution.get_length(head1)
        list2_len = Solution.get_length(head2)

        if list1_len >= list2_len:
            long_node, short_node = head1, head2
            diff = list1_len - list2_len

        else:
            long_node, short_node = head2, head1
            diff = list2_len - list1_len

        for _ in range(diff):
            long_node = long_node.next

        while long_node is not short_node:
            long_node = long_node.next
            short_node = short_node.next

        return long_node

# Assume the following Node class is already defined:
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# A helper to print a list (for debugging)
def print_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(str(cur.data))
        cur = cur.next
    print(" -> ".join(vals))


# --------------- Test Case 1 ---------------
# List1: 4 -> 1 -> 8 -> 4 -> 5
# List2: 5 -> 6 -> 1
# Intersection starts at the node with value 8 (the third node of List1).

# 1) Build the “shared tail” [8 -> 4 -> 5].
shared = create_linked_list([8, 4, 5])

# 2) Build the unique prefixes, then attach “shared” onto their tails.
head1 = create_linked_list([4, 1])
tail1 = head1
while tail1.next:
    tail1 = tail1.next
tail1.next = shared
# Now head1 is 4->1->(8->4->5)

head2 = create_linked_list([5, 6, 1])
tail2 = head2
while tail2.next:
    tail2 = tail2.next
tail2.next = shared
# Now head2 is 5->6->1->(8->4->5)

sol = Solution()
intersection_node = sol.intersectPoint(head1, head2)
print("Test 1 intersection:", intersection_node.data if intersection_node else None)
# Expected output: 8



# --------------- Test Case 2 ---------------
# List1: 1 -> 9 -> 1 -> 2 -> 4
# List2: 3 -> 2 -> 4
# Intersection starts at node with value 2 (fourth node in List1).

shared = create_linked_list([2, 4])

head1 = create_linked_list([1, 9, 1])
tail1 = head1
while tail1.next:
    tail1 = tail1.next
tail1.next = shared
# head1 is now 1->9->1->(2->4)

head2 = create_linked_list([3])
tail2 = head2
while tail2.next:
    tail2 = tail2.next
tail2.next = shared
# head2 is now 3->(2->4)

intersection_node = sol.intersectPoint(head1, head2)
print("Test 2 intersection:", intersection_node.data if intersection_node else None)
# Expected output: 2



# --------------- Test Case 3 ---------------
# List1: 2 -> 6 -> 4
# List2: 1 -> 5
# *No intersection* (for robustness)—we’ll return None in this scenario.

head1 = create_linked_list([2, 6, 4])
head2 = create_linked_list([1, 5])

intersection_node = sol.intersectPoint(head1, head2)
print("Test 3 intersection:", intersection_node.data if intersection_node else None)
# Expected output: None  (since no shared node)



# --------------- Test Case 4 ---------------
# List1: 0 -> 9 -> 1 -> 2 -> 4 -> 6
# List2:       3 -> 2 -> 4 -> 6
# Intersection starts at node with value 2, but here the unique prefixes have different lengths.

shared = create_linked_list([2, 4, 6])

# Build List1 = [0, 9, 1] + shared
head1 = create_linked_list([0, 9, 1])
tail1 = head1
while tail1.next:
    tail1 = tail1.next
tail1.next = shared
# head1 = 0->9->1->(2->4->6)

# Build List2 = [3] + shared
head2 = create_linked_list([3])
tail2 = head2
while tail2.next:
    tail2 = tail2.next
tail2.next = shared
# head2 = 3->(2->4->6)

intersection_node = sol.intersectPoint(head1, head2)
print("Test 4 intersection:", intersection_node.data if intersection_node else None)
# Expected output: 2



# --------------- Test Case 5 (Intersection at head) ---------------
# List1: 7 -> 8 -> 9
# List2: (the same exact list)
# In this scenario, the intersection is at the very first node (value 7).

head1 = create_linked_list([7, 8, 9])
head2 = head1  # point both heads to the same list

intersection_node = sol.intersectPoint(head1, head2)
print("Test 5 intersection:", intersection_node.data if intersection_node else None)
# Expected output: 7
