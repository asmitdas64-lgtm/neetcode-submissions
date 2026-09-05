class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = [] 
        n = len(nums)

        nums.sort()

        def dfs(i):
            res.append(sol[:])
            for j in range(i,n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                sol.append(nums[j])
                dfs(j+1)
                sol.pop()
    
        dfs(0)
        return res