def permute(nums):
    
    
    def dfs(nums, path, res):
        if(not nums):
            res.append(path)
            
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
    res = []
    dfs(nums, [], res)
    return res

input = [1,2,3,4,5,6,7]
print(permute(input))