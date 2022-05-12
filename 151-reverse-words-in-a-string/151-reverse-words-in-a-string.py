class Solution:
    def reverseWords(self, s: str) -> str:
        l= s.split()
        l.reverse()
        
        r=''
        for i in l:
            r+=i
            r+=' '
        
        return r[:-1]