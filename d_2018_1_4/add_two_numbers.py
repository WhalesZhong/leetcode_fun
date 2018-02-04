# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = l1.val + l2.val
        key = 0
        if num >= 10:
            key = 1
            num -= 10

        res_node = ListNode(num)
        node = res_node
        l1 = l1.next
        l2 = l2.next

        while (l1 or l2):
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + key
            key = 0
            if num >= 10:
                key = 1
                num -= 10

            new_node = ListNode(num)
            node.next = new_node
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if key == 1:
            node.next = ListNode(1)

        return res_node


if __name__ == '__main__':

    node = ListNode(2)
    node.next = ListNode(4)
    node.next.next = ListNode(3)

    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)

    s = Solution()
    s.addTwoNumbers(node, node2)

