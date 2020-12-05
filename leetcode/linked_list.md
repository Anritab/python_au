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
