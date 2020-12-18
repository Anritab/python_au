## Valid Anagram
https://leetcode.com/problems/valid-anagram/
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)
        if a == b:
            return True
        else:
            return False
```
