class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number0 = 0
        number1 = 1
        while number0 != len(nums) :
            while number1 != len(nums) :
                if number0 != number1 and nums[number0] + nums[number1] == target :
                    print (str(number0) + " " + str(number1))
                    return [number0,number1]
                    break
                else :
                    number1 += 1
            number1 = 1
            number0 += 1
