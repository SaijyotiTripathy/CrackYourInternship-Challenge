class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def triSum(nums):
            l=[]
            for i in range(len(nums)-1):
                l.append((nums[i]+nums[i+1])%10)
            if len(l)==1:
                return l[0]
            else:
                return triSum(l)
                
        return triSum(nums)
        