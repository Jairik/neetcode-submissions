class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
        '''
        #Base Case
        if len(s) != len(t):
            return False
        
        temp = list(s)
        for i in range(len(t)):
            if t[i] in temp:
                temp.remove(t[i])
            else:
                return False
            
        return True