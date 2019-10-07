from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.recurse([], nums)
        return self.res

    def recurse(self, used: List[int], nums: List[int]):
        if len(used) == len(nums):
            self.res.append(used)
            return
        for i in nums:
            if i not in used:
                list = used.copy()
                list.append(i)
                self.recurse(list, nums)


res = Solution().permute([1, 2, 3, 4, 5])
print(len(res))
