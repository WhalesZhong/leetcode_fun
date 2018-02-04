# coding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_node_from_end_of_list(head, n):
    """

    :param head:
    :type head: ListNode
    :param n:
    :return:
    """
    def remove_node(node, n):
        if node.next:
            k = remove_node(node.next, n)
            k += 1
        else:
            k = 0

        if k == n:
            node.next = node.next.next
        return k

    k = remove_node(head, n)
    return head.next if k < n else head


