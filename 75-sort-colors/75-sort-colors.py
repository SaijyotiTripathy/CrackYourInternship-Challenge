class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,mid,r=0,0,len(nums)-1
        while mid<=r:
            if nums[mid]==0:
                nums[mid],nums[l]=nums[l],nums[mid]
                l+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[r]=nums[r],nums[mid]
                r-=1
        
        