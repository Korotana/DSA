from LinkedList.CreateLinkedList import create_linked_list
from LinkedList.Node import Node
from LinkedList.PrintLinkedList import print_linked_list


class Solution:
    def sortedMerge(self, head1, head2):
        # code here

        merged_list = Node(0)
        merged_list_tail = merged_list

        while head1 and head2:
            if head1.data <= head2.data:
                merged_list_tail.next, head1 = head1, head1.next
            else:
                merged_list_tail.next, head2 = head2, head2.next
            merged_list_tail = merged_list_tail.next

        merged_list_tail.next = head1 if head1 else head2

        return merged_list.next

def linked_list_to_list(head):
    """Convert a linked list back to a Python list for easy comparison."""
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out


def run_merge_tests():
    sol = Solution()
    tests = [
        # name                 list A             list B            expected merged order
        ("both empty",          [],               [],               []),
        ("A empty",             [],               [1, 2, 3],        [1, 2, 3]),
        ("B empty",             [4, 5],           [],               [4, 5]),
        ("single nodes",        [1],              [0],              [0, 1]),
        ("all duplicates",      [1, 1, 1],        [1, 1],           [1, 1, 1, 1, 1]),
        ("non-overlapping",     [1, 2, 3],        [10, 20],         [1, 2, 3, 10, 20]),
        ("alternating",         [1, 3, 5, 7],     [2, 4, 6, 8],     [1, 2, 3, 4, 5, 6, 7, 8]),
        ("A much longer",       [0, 2, 4, 6, 8],  [1],              [0, 1, 2, 4, 6, 8]),
        ("B much longer",       [7],              [1, 3, 5, 9, 11], [1, 3, 5, 7, 9, 11]),
        ("negatives & zeros",   [-5, -3, 0, 2],   [-4, -1, 1],      [-5, -4, -3, -1, 0, 1, 2]),
    ]

    any_fail = False
    for name, a_vals, b_vals, expected in tests:
        a = create_linked_list(a_vals)  # helper you already have
        b = create_linked_list(b_vals)
        merged = sol.sortedMerge(a, b)
        got = linked_list_to_list(merged)
        if got != expected:
            any_fail = True
            print(f"❌  {name} FAILED – expected {expected}, got {got}")
        else:
            print(f"✅  {name} passed")

    if not any_fail:
        print("\n🎉  All edge-case tests passed!")


if __name__ == "__main__":
    # original demo
    h1 = create_linked_list([5, 10, 15, 40])
    h2 = create_linked_list([2, 3, 20])
    sol = Solution()
    merged_head = sol.sortedMerge(h1, h2)
    print("Merged list:")
    print_linked_list(merged_head)
    print()

    # run edge-case suite
    run_merge_tests()