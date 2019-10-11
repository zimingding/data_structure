from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            val = nums[i]
            idx = 0
            for j in range(i-1, -1, -1):
                if nums[j] > val:
                    nums[j+1] = nums[j]
                else:
                    idx = j + 1
                    break
            nums[idx] = val
        return nums


print(Solution().sort([6, 5, 4, 1, 3, 2]))
