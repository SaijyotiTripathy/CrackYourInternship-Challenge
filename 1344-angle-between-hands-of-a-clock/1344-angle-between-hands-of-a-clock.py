class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            angle= math.fabs(6*minutes - (30*math.fabs(hour-12) + 0.5*minutes))
        else:
            angle= math.fabs(6*minutes - (30*hour + 0.5*minutes))
        
        return min(angle,360-angle)