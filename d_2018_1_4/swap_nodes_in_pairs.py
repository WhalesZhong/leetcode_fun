# coding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_nodes_in_pairs(head):
    """

    :param head:
    :type head: ListNode
    :return:
    """

    if head:
        if head.next:
            new_head = head.next
            head.next = new_head.next
            new_head.next = head
            head.next = swap_nodes_in_pairs(head.next)
            return new_head
        else:
            return head
    else:
        return None


