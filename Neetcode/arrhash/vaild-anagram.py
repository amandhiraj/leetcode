#Coded by Aman Dhiraj

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapL = Counter(s)
        if len(s) != len(t):
            return False
        for char in t :
            if char in mapL:
                mapL[char] = mapL[char] - 1
        for i in mapL:
            if mapL[i] > 0 or mapL[i] < 0:
                return False
        return True