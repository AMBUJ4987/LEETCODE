class Solution:
    def shiftingLetters(self, s, shifts):
        result = []
        total = 0

        for i in range(len(s) - 1, -1, -1):
            total += shifts[i]
            shift = total % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result[::-1])