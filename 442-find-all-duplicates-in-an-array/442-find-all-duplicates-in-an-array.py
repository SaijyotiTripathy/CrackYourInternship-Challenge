class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d= Counter(nums)  #O(n)
        
        return list(i for i in d if d[i]==2)
            
        