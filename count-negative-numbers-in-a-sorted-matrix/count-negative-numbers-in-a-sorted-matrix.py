class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalnegative = 0
        for i in grid:
            for j in i:
                if j < 0:
                    totalnegative += 1
        
        return totalnegative
