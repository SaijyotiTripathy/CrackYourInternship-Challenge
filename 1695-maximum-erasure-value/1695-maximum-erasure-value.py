class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        prev_max,add,j= 0,0,0
        
        for i in range(len(nums)):
            while j<i and nums[i] in s:
                s.remove(nums[j])
                add-= nums[j]
                j+=1
            add+= nums[i]
            s.add(nums[i])
            prev_max= max(prev_max, add)
        return prev_max
            