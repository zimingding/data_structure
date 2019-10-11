from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_val = 2 ** 32
            idx = 0
            for j in range(i, n):
                if nums[j] < min_val:
                    min_val = nums[j]
                    idx = j
            nums[i], nums[idx] = nums[idx], nums[i]
        return nums


print(Solution().sort([6, 5, 4, 1, 3, 2]))
