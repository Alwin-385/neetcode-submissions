class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts,countt={},{}
        for i in s:
            counts[i]=counts.get(i,0)+1
        for i in t:
            countt[i]=countt.get(i,0)+1
        return counts==countt

        
            
