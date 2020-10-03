class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        #Return where element only found at path[1]
        return_list = []
        for i in paths :
            for j in i :
                return_list.append(j)

        return_list2 = []
        for i in paths :
            return_list2.append(i[0])

        return_list3 = list(set(return_list) - set(return_list2))
        
        return_string = ""
        for i in return_list3 :
            return_string += i
        return return_string
