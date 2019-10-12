from typing import List


class Solution:
    def quick_sort(self, nums: List[int]):
        self.quick_sort_c(nums, 0, len(nums)-1)

    def quick_sort_c(self, nums: List[int], p: int, r: int):
        if p >= r:
            return

        q = self.partition(nums, p, r)

        self.quick_sort_c(nums, p, q-1)
        self.quick_sort_c(nums, q+1, r)

    def partition(self, nums: List[int], p: int, r: int) -> int:
        i = p
        for j in range(i, r):
            if nums[j] < nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
