class Solution:
    def isPalindrome(self, head):
            # write your code here
            if head==None or head.next==None:
                return True

            pre = []
            while head:
                pre.append(head.val)
                head = head.next

            length = len(pre)
            for i in range(0, int(length/2)):
                if pre[i] != pre[length-i-1]:
                    return False
            return True

#solution2 (from coder_orz CSDN:http://blog.csdn.net/coder_orz/article/details/51306985)
#时间复杂度O(n)，空间复杂度O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next # slow指向链表的后半段
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head


# Solution3 76ms LeetCode beat 100%
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        tempArr = []

        while curr is not None:
            tempArr.append(curr.val)
            curr = curr.next

        if tempArr[::-1] != tempArr:
            return False

        return True