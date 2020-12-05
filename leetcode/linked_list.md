## Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
```python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev
```
## Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
```python
def middleNode(self, head: ListNode) -> ListNode:
    l = 0
    n = head
    while head:
        l += 1
        head = head.next     
    i = 0
    while i < l // 2 and n:
        n = n.next
        i += 1
    return n
```
## Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/submissions/
```python
def isPalindrome(self, head: ListNode) -> bool:
    list = []
    while head:
        list.append(head.val)
        head = head.next
    i = 0
    j = len(list) - 1
    while i < j:
        if list[i] != list[j]:
            return 0
        i += 1
        j -= 1
    return 1
```
## Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
```python
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        res = None
        while l1 or l2:
            if (l1 and not l2) or (l1 and l1.val <= l2.val):
                if not result:
                    result = l1
                    res = l1
                else:
                    res.next = l1
                    res = res.next
                l1 = l1.next
            else:
                if not result:
                    result = l2
                    res = l2
                else:
                    res.next = l2
                    res = res.next
                l2 = l2.next
        return result
```
## Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    a = ListNode(0)
    a.next = head
    node = a
    nodes = []
    while node:
        nodes.append(node)
        node = node.next

    i = len(nodes) - n - 1
    node = nodes[i]
    node.next = node.next.next

    return a.next
```
## Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
```python
def detectCycle(self, head: ListNode) -> ListNode:
    t = head
    d = {}
    while t:
        if t not in d:
            d[t] = 1
        else:
            return t
        t = t.next
    return None
```
