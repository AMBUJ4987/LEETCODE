class Solution:
    def kthCharacter(self, k: int) -> str:

        s1 = 'a'
        s2 = ""
        while len(s1)<k:
            for char in s1:
                s2 += chr(ord(char) + 1)
            s1 += s2
            s2= ""
        return s1[k-1]
        