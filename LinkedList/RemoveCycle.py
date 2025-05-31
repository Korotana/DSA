

class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here

        fast = head
        slow = head

        if head is None or head.next is None:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return

        slow = head

        if fast == slow:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return

        while slow.next != fast.next:
            slow, fast = slow.next, fast.next

        fast.next = None
        return



