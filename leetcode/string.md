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
## Reverse String
https://leetcode.com/problems/reverse-string/
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = []
        for i in range(len(s) - 1, -1, -1):
            a.append(s[i])
        s.clear()
        s.extend(a)
```
## Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        glasnie = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = []
        b = []
        s = list(s)
        for i, j in enumerate(s):
            if j in glasnie:
                b.append(i)
                a.append(j)
        a = a[::-1]
        for i, j in enumerate(b):
            s[j] = a[i]
        return ''.join(s)
```
## Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        b = [c[::-1] for c in a]
        return (' '.join(b))
```
## To Lower Case
https://leetcode.com/problems/to-lower-case/
```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        for i in str:
            if ord(i) > 64 and ord(i) < 91:
                s += chr(ord(i) + 32)
            else:
                s += i     
        return s
```
