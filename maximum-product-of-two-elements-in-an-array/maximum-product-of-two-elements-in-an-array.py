class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        location = 0
        for i in range(len(nums)) :
            if nums[i] > largest :
                largest = nums[i]
                location = i
        del nums[location]
        
        largest_2 = nums[0]
        location_2 = 0
        for i in range(len(nums)) :
            if nums[i] > largest_2 :
                largest_2 = nums[i]
                location_2 = i
        del nums[location_2] 
        
        
        #print nums
        
        return (largest - 1) * (largest_2 - 1)
               
        #print ( nums[0] - 1 ) * ( nums[1] - 1 )
