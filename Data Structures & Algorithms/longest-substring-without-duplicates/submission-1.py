class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first=0
        maxlen=1
        unique={}
        if s == "":
            return 0
        for second in range(0,len(s)):
            if s[second] in unique and unique[s[second]]>=first:
                first=unique[s[second]]+1
            unique[s[second]]=second
            maxlen=max(maxlen,second-first+1)
        return maxlen

        