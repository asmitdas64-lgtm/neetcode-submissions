class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        
        n = len(nums)

        nums.sort()

        def dfs(i,total):
            if total == target:
                res.append(sol[:])
                return
            if total > target or i >= n:
                return 
            
            dfs(i+1,total)


            sol.append(nums[i])
            dfs(i,total + nums[i])
            sol.pop()
        dfs(0,0)
        return res
