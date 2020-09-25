class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        counter = 0
        
        while index < len(nums) :
            if len(str(nums[index])) % 2  == 0:
                counter += 1
            index += 1
            
        return counter
