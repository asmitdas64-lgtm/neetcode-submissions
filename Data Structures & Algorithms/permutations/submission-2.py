class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        nums.sort()
        self.seen = set()
        
        def dfs(i):
            if i == n:
                res.append(sol[:])
                return 
            
            for j in range(n):
                if j not in self.seen:
                    self.seen.add(j)
                    sol.append(nums[j])
                    dfs(i+1)
                    sol.pop()
                    self.seen.remove(j)


        dfs(0)
        return res


            
            
            


