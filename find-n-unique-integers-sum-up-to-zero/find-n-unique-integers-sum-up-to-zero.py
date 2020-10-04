import math
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #If n is an odd number, return n - 1 numbers and 0, where half are positve and the other half are the negative version of that number
        #If n is an even number, return n numbers, where half are positve and the other half are the negative version of that number
        #print n
        
        #print math.floor( 7/2 )
        
        return_array = []
        
        counter = 1
        while counter <= int(math.floor(n/2)) :
            #print counter
            return_array.append(counter)
            return_array.append(counter * -1)
            counter += 1
        
        if n % 2 != 0 :
            return_array.append(0)
        
        return list(return_array)
        
        #for i in range(int(math.floor(n/2))):
        #    print i
