## Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return None
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1
```
## Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a = []
        if not root:
            return None
        if root.left:
            a += self.inorderTraversal(root.left)
        a.append(root.val)
        if root.right:
            a += self.inorderTraversal(root.right)
        return a
```
## Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            l = self.invertTree(root.left)
            r = self.invertTree(root.right)
            root.left = r
            root.right = l
        return root
```
## Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
```python

```
## Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python

```
## Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python

```
## Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python

```
## Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python

```
