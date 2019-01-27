class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #treat as string
        s = str(x)
        
        #one digit => true
        if(len(s) == 1):
            return True
        
        #negative number
        if(x < 0):
            return False
        
        #reverse and then split in half 
        #removes middle number is odd
        print(s)
        r = s[::-1]
        s = s[:int(len(s)/2)]
        r = r[:int(len(r)/2)]
        
        if(s == r):
            return True
        
        
        
        return False
    