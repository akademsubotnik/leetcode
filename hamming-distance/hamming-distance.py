class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z0,z1,int_difference = "{0:b}".format(x),"{0:b}".format(y),0
        list_z0,list_z1 = list(z0),list(z1)
        
        
        if len(list_z0) > len(list_z1) :
            #If z0 is larger than z1
            while len(list_z0) != len(list_z1) :
                list_z1.insert(0,'0')
        if len(list_z0) < len(list_z1) :
            while len(list_z0) != len(list_z1) :
                #If z1 is larger than z0
                list_z0.insert(0,'0')

        
        i = 0
        while i < len(list_z0) :
            if list_z0[i] != list_z1[i] :
                int_difference += 1       
            i += 1
        
        return int_difference
