class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        #g : --.
        #i : ..
        #n : -.
        
        #--. .. -.
        
        #z : --..
        #e : .
        #n : -.
        
        #--.. . -.
        
        alphabet_dict = {"a":".-", "b":"-...", "c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."};

        morse_array = []
        for i in words:
            tmp_str = ""
            for j in i:
                tmp_char =  alphabet_dict.get(j)
                tmp_str = tmp_str + tmp_char
            morse_array.append(tmp_str)
              
        #print morse_array
        #print words
        
        #check unique values in morse_array
        #for i in (morse_array) :
        myset = set(morse_array) 
        return len(myset)
