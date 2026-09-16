class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        [1,2,2,4,5,6,9]
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(idx, path, total):
            if total == target:
                ans.append(path[:])
                return
            if idx >= len(candidates):
                return

            new_total = total + candidates[idx]
            if new_total > target:
                return
            
            path.append(candidates[idx])
            backtrack(idx+1, path, new_total)
            path.remove(candidates[idx])
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx+1, path, total)

        backtrack(0, [], 0)
        return ans

        