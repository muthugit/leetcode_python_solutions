# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def convertToList(self, nodeIP):
        li = []
        while nodeIP is not None:
            li.append(nodeIP.val)
            nodeIP = nodeIP.next
        return li

    def convertToListNode(self, listIP):
        root = ListNode(0)
        ne = root
        for i in listIP:
            ne.next = ListNode(i)
            ne = ne.next
        return root.next


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.convertToList(l1)
        n2 = self.convertToList(l2)
        big_list = n1 if len(n1)>=len(n2) else n2
        small_list = n1 if len(n1)<len(n2) else n2
        result = []
        remainder = 0
        for i in range(len(big_list)):
            if len(small_list) > i:
                t = int(big_list[i]) + int(small_list[i]) + remainder
                result.append(t%10)
                remainder = int(t/10)
            else:
                t = int(big_list[i]) + remainder
                result.append(t%10)
                remainder = int(t/10)
        if remainder:
            result.append(remainder)
        return self.convertToListNode(result)
