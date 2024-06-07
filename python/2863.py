class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)    
                # find from last to start: large to small 
        # stack number is increasing from top to bottom 
        
        r = 0
        m = float('-inf')      
        for i in range(n):
            # i: left pointer, stack element: right pointer
            while stack and stack[-1] <= i:
                stack.pop() 
                # if left pointer index is larger than right pointer index 
                  
            if nums[i] > m:
                m = nums[i]  
                while stack and nums[stack[-1]] < m:
                    r = max(r, stack[-1] - i + 1)
                    stack.pop() 
                    # try next larger value in stack 
                    # next value in the stack must be the next larger value in nums
        return r