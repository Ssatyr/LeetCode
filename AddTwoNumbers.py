class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        ptr = result
        mem = 0

        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            ptr.next = ListNode((v1 + v2 + mem)%10)
            ptr = ptr.next

            mem = (v1 + v2 + mem)//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if mem > 0:
            ptr.next = ListNode(mem)


        return result.next
