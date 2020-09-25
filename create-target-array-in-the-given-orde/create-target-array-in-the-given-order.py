class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target,i = [],0
        
        while (i < len(nums)) and (i < len(index)) : 
            # Insert nums[i] into target at index[i] 
            target.insert(index[i],nums[i])
            i += 1
        return target
