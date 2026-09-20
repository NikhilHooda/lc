class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, ans = 0, []
        queue = collections.deque()

        for r in range(len(nums)):
            # step 1: add new element to queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # step 2: remove from left side of queue
            if l > queue[0]:
                queue.popleft()
            
            # step 3: add to output
            if (r + 1) >= k:
                ans.append(nums[queue[0]])
                l += 1
        return ans



            

        