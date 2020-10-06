class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return_list = []
        
        for i in A :
            if i % 2 == 0 :
                return_list.append(i)

        for i in A :
            if i % 2 != 0 :
                return_list.append(i)

        
        return return_list
