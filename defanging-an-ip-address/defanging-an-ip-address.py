class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        straddress = address.encode('ascii','ignore') #Encode to string
        straddress = straddress.replace(".","[.]")
        return straddress
