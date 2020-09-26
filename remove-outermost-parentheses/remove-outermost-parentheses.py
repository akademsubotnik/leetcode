class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        #If next parentheses is not different, remove it
        #print S
        str_return = ""
        
        for counter in range(len(S) - 1):
            if S[counter] != S[counter + 1] :
                str_return = str_return + S[counter]
        
        if str_return[len(str_return) - 1] != ')' :
            str_return = str_return + ')'
        
        print str_return
        return str_return
            
        #()()()()(())
