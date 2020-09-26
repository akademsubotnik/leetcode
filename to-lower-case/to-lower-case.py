class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str_return = ""
        
        for counter in range(len(str)) :
            if str[counter].isupper() :
                str_return = str_return + str[counter].lower()
            else :
                str_return = str_return + str[counter]
        return str_return
