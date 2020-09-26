class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        counter = 0
        str_return = []
        
        for counter in range(len(str)) :
            if str[counter].isupper() :
                #print "is upper"
                str_return.append(str[counter].lower())
            else :
                str_return.append(str[counter])
        #return str_return
        
        str_3 = ""
        for counter in range(len(str_return)) :
            str_3 = str_3 + str_return[counter]
        return str_3
