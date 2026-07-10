class Solution:
    def chardict(self,s1):
        s1chars={}
        for char in s1:
            if char in s1chars:
                s1chars[char]+=1
            else:
                s1chars[char]=1
        return s1chars
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1chars=self.chardict(s1)
        for i in range(len(s2)-len(s1)+1):
            if s1chars==self.chardict(s2[i:i+len(s1)]):
                return True
        return False
            

        