class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        #Step 1: Remove outermost parentheses
        str_return = ""
        str_return = S[1:len(S) - 1]
        
        #If next parentheses is not different, remove it
        
        #for counter in range (len(str_return)) :
        counter = 0
        while counter < (len(str_return) - 1) :
            if str_return[counter] == str_return[counter + 1] :
                str_return = str_return[0:counter] + str_return[counter+1:]
            counter += 1
        return str_return
