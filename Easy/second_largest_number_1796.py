class Solution:
    def secondHighest(self, s: str) -> int:
        first_max = -1
        second_max = -1

        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit > first_max:
                    second_max = first_max
                    first_max = digit
                elif first_max > digit > second_max:
                    second_max = digit

        return second_max


obj = Solution()
s = "dfa12321afd"
print(obj.secondHighest(s))
