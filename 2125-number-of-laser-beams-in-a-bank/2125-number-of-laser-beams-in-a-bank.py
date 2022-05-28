class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        prev=0
        for i in bank:
            new=0
            for j in i:
                if j=='1':
                    new+=1
            res+= prev*new
            if new!=0:
                prev=new
        return res