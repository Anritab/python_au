## Reverse Integer
```python
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        x = str(x)  #почему
        y = ""
        for i in range(len(x) - 1, -1, -1):
            y += x[i]
        y = int(y)  #потому
        if flag == 1:
            y = - y
        if y > 2 ** 31 - 1 or y < - 2 ** 31:
            return 0
        return y
```
