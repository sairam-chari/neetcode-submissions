class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            data=[]
            for i in range(len(position)):
                data.append((position[i],speed[i]))
            data.sort()
            time=[]
            fleets=1
            for pos,vel in data:
                time.append((target-pos)/vel)
            for i in range(len(time)-2,-1,-1):
                t=time[i]
                tf=time[i+1]
                if t<=tf:
                    time[i]=tf
                else:
                    fleets+=1
            return fleets



