class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars={}
        first=0
        second=0
        maxlen=0
        # if len(s)==0:
        #     return 0
        for i in range(len(s)):
            if s[i] in chars and first<=chars[s[i]]:
                first=chars[s[i]]+1
                chars[s[i]]=i
            else:
                chars[s[i]]=i
                maxlen=max(maxlen,(i-first+1))
        return maxlen

            
        