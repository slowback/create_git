# Definition for singly-linked list.

#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __repr__(self):
#         return f'ListNode(val={self.val}, next={self.next})'
#
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#
#         """
#         head = ListNode(0)
#         result_tail = head
#         carry = 0
#
#         while l1 or l2 or carry:
#             val1 = (l1.val if l1 else 0)
#             val2 = (l2.val if l2 else 0)
#             carry, out = divmod(val1 + val2 + carry, 10)
#
#             result_tail.next = ListNode(out)
#             result_tail = result_tail.next
#
#             l1 = (l1.next if l1 else None)
#             l2 = (l2.next if l2 else None)
#
#         return head.next


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
