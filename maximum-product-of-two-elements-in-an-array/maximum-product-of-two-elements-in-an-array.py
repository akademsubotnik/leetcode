class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, location = nums[0],0
        
        for i in range(len(nums)) :
            if nums[i] > largest :
                largest = nums[i]
                location = i
        del nums[location]
        del location
        
        largest_2,location_2 = nums[0],0
        
        for i in range(len(nums)) :
            if nums[i] > largest_2 :
                largest_2 = nums[i]
                location_2 = i
        del nums[location_2] 
        del location_2
        
        
        return (largest - 1) * (largest_2 - 1)
