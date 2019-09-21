from typing import List


class Array:
    def merge(self, a: List, b: List) -> List:
        res = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        return res + a[i:] + b[j:]


print(Array().merge([1, 3, 5], [2, 4, 6]))
