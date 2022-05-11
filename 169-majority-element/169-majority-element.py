class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)    #O(n)
        l= Counter(nums)     #O(n)
        
        return l.most_common(1)[0][0]      #O(n)