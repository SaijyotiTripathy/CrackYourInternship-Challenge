class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs, curs= '',''
        
        for i in s:
            if i not in curs:
                curs+=i
                if len(curs)>= len(maxs):
                    maxs=curs
            else:
                curs= curs[curs.index(i)+1:]+i
                
            #print(curs, maxs)
        return len(maxs)