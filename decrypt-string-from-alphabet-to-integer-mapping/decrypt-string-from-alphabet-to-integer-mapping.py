class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        transform_dict = {"1":'a',"2":'b',"3":'c',"4":'d',"5":'e',"6":'f',"7":'g',"8":'h',"9":'i',"10#":'j',"11#":'k',"12#":'l',"13#":'m',"14#":'n',"15#":'o',"16#":'p',"17#":'q',"18#":'r',"19#":'s',"20#":'t',"21#":'u',"22#":'v',"23#":'w',"24#":'x',"25#":'y',"26#":'z'};
        
        return_array = []
        i = 0
        while i < len(s) :
            tmp_str = ""
            #The next characters must be 1-9 (if there are characters)
            if i+2 >= len(s):
                return_array.append(transform_dict.get(s[i]))
                i += 1
                pass
            elif (s[i] == '#') :
                i += 1
                pass
            #Get the next two characters, they are (10#-26#)
            elif (s[i+2] == '#') :
                tmp_str = s[i] + s[i+1] + "#"
                return_array.append(transform_dict.get(tmp_str))
                i += 2
                pass
            else :
                return_array.append(transform_dict.get(s[i]))
                i += 1
        
        return_string = ""
        for i in range(len(return_array)):
            if return_array[i] != None :
                return_string += str(return_array[i])
            
        return return_string
            
            
