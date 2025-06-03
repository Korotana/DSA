'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''


class Solution:

    def sortedMerge(self, head1, head2):

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

    def mergeKLists(self, arr):
        # code here
        # return head of merged list

        if not arr:
            return None

        while len(arr) > 1:
            merged_level = []
            for i in range(0, len(arr), 2):
                head1, head2 = arr[i], arr[i + 1] if i + 1 < len(arr) else None
                merged_level.append(self.sortedMerge(head1, head2) if head2 else head1)

            arr = merged_level

        return arr[0]