#reversing a linked lise

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        stack = []

        curr_node = head
        while curr_node.next != null
            stack.append(curr_node)
            curr_node = curr_node.next


        stack = stack.reverse()
        head = stack[1]
        return head
