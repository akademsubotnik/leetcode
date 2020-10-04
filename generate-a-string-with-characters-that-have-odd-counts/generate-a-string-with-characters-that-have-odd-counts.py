class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return_array = []
        if n % 2 == 0 :
            for i in range(n - 1) : 
                return_array.append('a')
            return_array.append('z')
        else :
            for i in range(n) :
                return_array.append('a')
        
        str_return = ""
        for i in range (len(return_array)) :
            str_return += return_array[i]
        
        return str_return
