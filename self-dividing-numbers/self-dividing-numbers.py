class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        dump_array = []
        for i in range(left,right+1) :
            if '0' not in str(i):
                dump_array.append(i)
        #print dump_array
        
        divisible_array = []
        for i in dump_array:
            #print i
            for j in range(0,len(str(i))) :
                #print str(i)
                if i % int(str(i)[j]) == 0 :
                    divisible_array.append(i)
        #print divisible_array
        
        #Go through the array and check if the number of entries for the number is equal to the number length, if it is add it to the next array, if it is not, do not add it to the next array
        
        array_removeduplicates = []
        for i in divisible_array : 
            #print i
            #print divisible_array.count(i)
            if divisible_array.count(i) == len(str(i)) :
                array_removeduplicates.append(i)
        
        #tmp_list = list(set(array_removeduplicates))
        
        #print array_removeduplicates
        
        res = [] 
        for i in array_removeduplicates : 
            if i not in res: 
                res.append(i) 
        
        return res
