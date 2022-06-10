class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1], reverse=True)
        n= len(boxTypes)
        
        i,res= 0,0
        while i<n:
            if boxTypes[i][0]>truckSize:
                break
            res+= boxTypes[i][0]*boxTypes[i][1]
            truckSize-= boxTypes[i][0]
            i+=1
        
        if i<n:
            res+= truckSize*boxTypes[i][1]
        
        return res