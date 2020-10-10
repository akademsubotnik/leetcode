from collections import Counter
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """      
        c = collections.Counter(A)
        
        for i in A:
            if c[i] == len(A)/2:
                return i
