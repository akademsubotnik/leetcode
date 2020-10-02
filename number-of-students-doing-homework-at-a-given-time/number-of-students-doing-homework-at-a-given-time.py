class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        
        working_return = []
        # If starttime[i] is less than or equal AND endtime[i] is greater than or equal to querytime
            #return true
        # else
            #return false
        
        i = 0
        
        while i < len(endTime) :
            if startTime[i] <= queryTime and endTime[i] >= queryTime :
                working_return.append(i)
            i += 1
        
        return len(working_return)
