class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        #Return where element only found at path[1]
        #print paths
        return_array = []
        for i in paths :
            for j in i :
                #print j
                return_array.append(j)
        #print return_array
        
        #myset = set(return_array) 
        #list comprehension -- to remove duplicates
        #https://stackoverflow.com/questions/26790493/remove-duplicates-and-original-from-list
        #https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
        #[item for item in lst if lst.count(item) == 1]
        #mylist = [a for a in return_array if return_array.count(a) == 1]
        #print mylist
        
        return_array2 = []
        for i in paths :
            return_array2.append(i[0])
            
        #print type(return_array)
        #print type(return_array2)
        
        #return_array3 = array(return_array) - array(return_array2)
        return_array3 = list(set(return_array) - set(return_array2))
        #print return_array3
        
        return_string = ""
        for i in return_array3 :
            return_string += i
        return return_string
