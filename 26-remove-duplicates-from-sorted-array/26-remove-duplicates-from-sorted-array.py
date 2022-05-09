class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        k = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == temp:
                continue
            nums[k] = nums[i]
            k += 1
            temp = nums[i]
        return k
    