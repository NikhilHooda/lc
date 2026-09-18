class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap of k largest elements
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
