class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        working_return,i = 0,0
        
        while i < len(endTime) :
            if startTime[i] <= queryTime and endTime[i] >= queryTime :
                working_return += 1
            i += 1
        
        return working_return
