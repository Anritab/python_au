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
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    def next(self) -> int:
        ans = self.stack.pop()
        root = ans
        root = root.right        
        if root:
            while root:
                self.stack.append(root)
                root = root.left
        return ans.val
    def hasNext(self) -> bool:
        return self.stack != []
```
## Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        curr_level = [root]
        if root is None:
            return []
        while curr_level:
            next_level = []
            node_values = []
            for n in curr_level:
                node_values.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            levels.append(node_values)
            curr_level = next_level
        return levels
```
## Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def inorder(node):
            if node == None:
                return
            nonlocal arr
            if len(arr) < k:
                inorder(node.left)
            if len(arr) < k:
                arr.append(node.val)
            if len(arr) < k:
                inorder(node.right)
        inorder(root)
        return arr[-1]
```
## Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        val = None
        while True:            
          if cur:
              stack.append(cur)
              cur = cur.left
          elif stack:
              cur = stack.pop()
              if val is not None and val >= cur.val:
                  return False
              val = cur.val
              cur = cur.right
          else:
              break
        return True
```
## Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
class Solution(object):
    
    def is_sym(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if (root1 == None and root2 != None) or (root1 != None and root2 == None):
            return False
        if root1.val !=root2.val:
            return False
        
        return self.is_sym(root1.right,root2.left) and self.is_sym(root1.left,root2.right)
    
    
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.is_sym(root.right,root.left)
```
