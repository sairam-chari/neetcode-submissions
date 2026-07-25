class Solution:

    def encode(self, strs: List[str]) -> str:
        lenarr=[]
        for s in strs:
            lenarr.append(len(s))
        return str(lenarr)+"".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        print(s)
        print(s.split("]"))
        lens, data = s.split("]")
        lens=lens[1:].split(",")
        outt=[]
        for i in range(len(lens)):
            lens[i]=int(lens[i])
        idx=0
        for l in lens:
            outt.append(data[idx:idx+l])
            idx+=l

        return outt