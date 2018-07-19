# 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.


**Example 1:**
```
Input: 1->2
Output: false
```

**Example 2:**
```
Input: 1->2->2->1
Output: true
```

**Follow up:**

Could you do it in O(n) time and O(1) space?



**Idea:**

我们不能用旋转所得的新链表与原链表相比较，因为相比较的是地址，而我们需要比较的是每一个节点的值(head.val)

而关于链表的问题经常会用到两个链表，一个快速，一个慢速来解决。类似的问题就有回文链表，删除链表中倒数第n个节点等等，这样的操作可以满足复杂度，但是可以AC但不满足复杂度要求的也有很多种解。

这道题要求的时间复杂度为n和空间复杂度均为1，所以我们不能用栈来存储值。

方法一：用新的list储存链表的val，转置list进行比较

方法二：通过快慢指针，快指针走到找到链表重点，对前半段链表转置，与后半段进行比较。


