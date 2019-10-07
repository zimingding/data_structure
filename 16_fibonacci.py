class Solution:
    def __init__(self):
        self.cache = {}

    def fibonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n in self.cache.keys():
            return self.cache[n]
        r = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.cache[n] = r
        return r
