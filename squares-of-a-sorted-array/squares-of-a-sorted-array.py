class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        powl = []
        for i in range(len(A)) :
            powl.append(pow(abs(A[i]),2))
        
        return sorted(powl)
