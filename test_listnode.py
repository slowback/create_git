# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __repr__(self):
    #     return f'ListNode(val={self.val}, next={self.next})'


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    s = Solution()
    for i1, i2 in zip(l1, l2):
        print(s.addTwoNumbers(ListNode(i1), ListNode(i2)))
