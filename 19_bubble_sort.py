from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


print(Solution().sort([6, 5, 4, 1, 3, 2]))
