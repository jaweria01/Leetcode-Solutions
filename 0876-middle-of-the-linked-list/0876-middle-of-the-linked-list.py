# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # step 1: count length
        temp = head
        count = 0
        while temp:
            count = count+1
            temp = temp.next


        # step 2: go to middle
        mid = count//2
        temp = head
        for i in range(mid): # (0,1)
            temp = temp.next 
        return temp

        # even = head//2
        # odd != head//2
        # mid = head//2
        # if head is even:
        #     return mid
        # else:
        #     mid +1
#TypeError: unsupported operand type(s) for //: 'ListNode' and 'int'(This error due to above code, as linkedlist not integer that can be divided , but it is object that store values of nodes)# 
# So try different method , it brute force

        # pointer1 = head
        # pointer2 = head
        # count = 0
        # while pointer1:
        #     count = count + 1
        #     pointer1 = pointer1.next
        # mid = count // 2

        # for i in range(mid):
        #     print("i",i)
        #     pointer2 = pointer2.next
        # return pointer2

    # Efficient Method below
        # slow = head
        # fast = head

        # while slow and slow.next: # This condition is checking slow instead of fast.#So, the loop can still run even when fast is already at the last node (or None).AttributeError: 'NoneType'(Last node is null) object has no attribute 'next'
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
#When fast reaches the end (or goes past it), slow will be exactly in the middle.

# 2nd Solution by converting linkedlist into list and then divide process, but its slow
        # nodes = []
        # while head:
        #     nodes.append(head)
        #     head = head.next
        # return nodes[len(nodes)//2]

        