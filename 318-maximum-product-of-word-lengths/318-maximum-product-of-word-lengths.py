class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        maxval=0
        
        for i in range(n):
            for j in range(i+1,n):
                if not set(words[i]).intersection(set(words[j])):
                    val= len(words[i])*len(words[j])
                    if val>maxval:
                        maxval= val
        
        return maxval
        