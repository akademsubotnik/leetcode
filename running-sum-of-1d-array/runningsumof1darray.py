class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Iniatilize
        index,indexsum,indexsum_array = 0,0,[]
        
        while index != len(nums) :
            indexsum = nums[index] + indexsum
            indexsum_array.append(indexsum)
            index += 1
        return indexsum_array
