from typing import List


class Solution:
    def heap_sort(self, nums: List[int]):
        n = len(nums)
        nums.insert(0, None)
        self.build_heap(nums, n)
        for i in range(n, 1, -1):
            nums[1], nums[i] = nums[i], nums[1]
            self.heapify(nums, i-1, 1)
        nums.pop(0)

    def build_heap(self, nums: List[int], n: int):
        for i in range(int(n/2), 0, -1):
            self.heapify(nums, n, i)

    def heapify(self, nums: List[int], n: int, i: int):
        while True:
            maxPos = i
            if i*2 <= n and nums[i*2] > nums[i]:
                maxPos = i*2
            if i*2+1 <= n and nums[i*2+1] > nums[maxPos]:
                maxPos = i*2+1
            if i == maxPos:
                break
            nums[i], nums[maxPos] = nums[maxPos], nums[i]
            i = maxPos


nums = [4,3,0,9,7,5,1]
Solution().heap_sort(nums)
print(nums)
