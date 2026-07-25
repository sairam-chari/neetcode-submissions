class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        fc=[]
        for s in strs:
            idx=-1
            freq=defaultdict(int)
            for c in s:
                freq[c]+=1
            for i in range(len(fc)):
                if fc[i]==freq:
                    idx=i
            if idx==-1:
                fc.append(freq)
                output.append([s])
            else:
                output[idx].append(s)
        return output
                

            
