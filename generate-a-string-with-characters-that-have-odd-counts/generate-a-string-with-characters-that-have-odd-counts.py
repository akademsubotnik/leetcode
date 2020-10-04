class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        str_return = ""
        if n % 2 == 0 :
            for i in range(n - 1) : 
                str_return += 'a'
            str_return += 'z'
        else :
            for i in range(n) :
                str_return += 'a'

        return str_return
