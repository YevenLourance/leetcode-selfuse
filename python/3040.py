class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j, score):
            if j-i> 0:
                first2 = nums[i]+nums[i+1]
                last2 = nums[j]+nums[j-1]
                first1last1 = nums[i]+nums[j]
                m = 0
                if first2 == score:
                    m = max(m, dfs(i+2,j,score)+1)
                if last2 == score:
                    m = max(m, dfs(i,j-2,score)+1)
                if first1last1 == score:
                    m = max(m, dfs(i+1,j-1,score)+1)
                return m
            else:
                return 0

        first2 = nums[0]+nums[1]
        last2 = nums[-2]+nums[-1]
        first1last1 = nums[0]+nums[-1]
        endidx = len(nums)-1

        return max(dfs(2, endidx, first2), dfs(0, endidx-2, last2), dfs(1, endidx-1, first1last1))+1
        
        