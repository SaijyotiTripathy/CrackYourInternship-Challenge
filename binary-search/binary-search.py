class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(nums,left,right,target)->int:
            if nums==[]:
                return -1
            
            if right<left:
                return -1

            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            
            elif target>nums[mid]:
                return binary(nums,mid+1,right,target)
            
            else:
                return binary(nums,left,mid-1,target)
    
        return binary(nums,0,len(nums)-1,target)