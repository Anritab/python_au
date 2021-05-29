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
## Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
```python
def hasCycle(self, head: ListNode) -> bool:
    t = head
    d = {}
    while t:
        if t not in d:
            d[t] = 1
        else:
            return True
        t = t.next
    return False
```
## Reorder List
https://leetcode.com/problems/reorder-list/
```python
def reorderList(self, head: ListNode) -> None:
    a = {}
    n = head
    while n and n.next != None:
        a[n.next] = n
        n = n.next

    start = head
    end = n
    while start != None and start != end:
        a[end].next = None
        end.next = start.next
        start.next = end
        start = end.next
        end = a[end]
```
## Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    tA, tB = headA, headB
    lenA, lenB = 0, 0
    while tA != None:
        lenA += 1
        tA = tA.next
    while tB != None:
        lenB += 1
        tB = tB.next
    if lenA > lenB:
        for i in range(lenA - lenB):
            headA = headA.next
    elif lenA < lenB:
        for i in range(lenB - lenA):
            headB = headB.next
    while headA != None and headB != None:
        if headA == headB:
            return headA
        headA, headB = headA.next, headB.next
    return None
```
## Sort List
https://leetcode.com/problems/sort-list/
```python
    def merged(self, head):
        x, y = head, head
        while x and x.next and x.next.next:
            x = x.next.next
            y = y.next
        return y
    def merge(self, l1, l2):
        x = ListNode(-1)
        h = x
        while l1 and l2:
            if l1.val < l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        if l1:
            h.next = l1
        else:
            h.next = l2
        return x.next
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        m = self.merged(head)
        nhead = m.next
        m.next = None
        left = self.sortList(head)
        right = self.sortList(nhead)
        return self.merge(left, right)
```
## Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
```python
class Solution(object):
	def mergeKLists(self, lists):
		l = []
		for i in lists:
			while i:
				l.append(i.val)
				i = i.next
		l.sort()
		print(l)
		head = ListNode()
		tmp = head
		for i in range(0,len(l)):
			tmp.next = ListNode(l[i])
			tmp = tmp.next
		return head.next
```
