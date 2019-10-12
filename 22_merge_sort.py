from typing import List


class Solution:
    def merge_sort(self, nums: List[int]):
        self.merge_sort_c(nums, 0, len(nums) - 1)

    def merge_sort_c(self, nums: List[int], p: int, r: int):
        if p >= r:
            return

        q = int((p + r) / 2)

        self.merge_sort_c(nums, p, q)
        self.merge_sort_c(nums, q + 1, r)

        self.merge(nums, p, q, r)

    def merge(self, nums: List[int], p: int, q: int, r: int):
        temp = []
        i = p
        j = q + 1
        while i <= q and j <= r:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        temp += nums[i:q + 1] + nums[j:r + 1]
        nums[p:r + 1] = temp


nums = [4, 5, 6, 1, 3, 2]
Solution().merge_sort(nums)
print(nums)
