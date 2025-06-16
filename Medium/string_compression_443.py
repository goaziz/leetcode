from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # position to write the compressed result
        read = 0   # position to read characters

        while read < n:
            char = chars[read]
            count = 0

            # Count how many times this char repeats
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count (only if >1), split digits into separate characters
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write


obj = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(obj.compress(chars))
