class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        #Step 1: Remove outermost parentheses
        str_return = ""
        str_return = S[1:len(S) - 1]
                
        #Input: "(()())(())(()(()))" Output: "()()()()()" Expected: "()()()()(())"
        #Input: "(()())(())" Expected: "()()()"
        # Step 2. Count LP/RP and make sure they are equal, if they are not equal, remove the correct LP or RP
        numlp,numrp = 0,0
        
        for counter in range (len(str_return)) :
            #If character is ( increment left parentheses counter
            if str_return[counter] == '(' :
                numlp += 1
            #There are only ( and ) if the string, if the character is not a (, it must be a )
            else :
                numrp += 1
        #Remove errant right parentheses     
        print "Len str_return: " + str(len(str_return))
        for counter in range (len(str_return) - 1) :
            print str(counter) + " " + str_return[counter]
            if counter == 0 :
                if (str_return[counter] == ')') :
                    #Remove right parentheses at str_return[0]
                    str_return = str_return[:counter] +  str_return[counter+1:]
            elif str_return[counter] == ')' and str_return[counter - 1] != '('  :
                #Remove the errant right parentheses )
                str_return = str_return[:counter] +  str_return[counter+1:]
        
        
        #Start at last index of string and then check going backward if there is a ( without a preceding )
        
        #print str_return
        counter01 = len (str_return) - 1
        while counter01 >= 0 :
            if str_return[counter01] == '(' and str_return[counter01 + 1] != ')' :
                #Remove the errant left parentheses (
                str_return = str_return[:counter01] +  str_return[counter01+1:]
            #print str_return[counter]
            counter01 -= 1
        return str_return
        
        #txt = "Hello World"[::-1]
        #str_return_reversed = str_return[::-1]
        #print "str_return: " + str_return
        #print "str_return_reversed: " + str_return_reversed
        
        
        #print "numlp: " + str(numlp)
        #print "numrp: " + str(numrp)
        #print "str_return:" + str_return
        
        
        # "(()())(())"
        # ()())(()
        # )(())()(
