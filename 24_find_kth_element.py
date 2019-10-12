from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = 0
        r = len(nums) - 1
        while True:
            q = self.partition(nums, p, r)
            if q == len(nums) - k:
                return nums[q]
            elif q < len(nums) - k:
                p = q + 1
            else:
                r = q - 1

    def partition(self, nums: List[int], p: int, r: int) -> int:
        i = p
        for j in range(i, r):
            if nums[j] < nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i


k = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3)
print(k)
