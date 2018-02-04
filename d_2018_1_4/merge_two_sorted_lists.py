# coding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_sorted_lists(l1, l2):
    """
    :param l1:
    :param l2:
    :type l1: ListNode
    :type l2: ListNode
    :return:
    """

    def merge(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = merge(l1.next, l2)
            return l1
        else:
            l2.next = merge(l1, l2.next)
            return l2

    if l1 and l2:
        return merge(l1, l2)
    else:
        return l1 or l2