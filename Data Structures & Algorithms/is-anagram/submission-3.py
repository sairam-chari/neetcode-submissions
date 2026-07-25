class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i=0
        sf=defaultdict(int)
        tf=defaultdict(int)
        if len(s)!=len(t):
            return False
        while i<len(s):
            sf[s[i]]+=1
            tf[t[i]]+=1
            i+=1
        if sf==tf:
            return True
        return False
                
        