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
