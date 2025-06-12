from typing import List


class Solution:
    def shift(self, word, n):
        letters = list(range(ord('a'), ord('z') + 1))
        idx = letters.index(ord(word))
        letter_idx = (idx + n) % len(letters)
        
        val = chr((ord(word) - 97 + n) % 26 + 97)

        return val

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = ""
        i, j = 0, len(s)
        shift_sum = sum(shifts) % 26
        prev_shift = 0

        while i < j:
            shift_sum = (shift_sum - prev_shift) % 26
            # result += self.shift(s[i], shift_sum)
            val = chr((ord(s[i]) - 97 + shift_sum) % 26 + 97)
            result += val
            prev_shift = shifts[i]
            i += 1

        return result


obj = Solution()
s = "bad"
shifts = [10, 20, 30]
print(obj.shiftingLetters(s, shifts))
