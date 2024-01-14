from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixels = []
        count = 0

        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if count + char_width > 100:
                pixels.append(count)
                count = char_width
            else:
                count += char_width

        if count > 0:
            pixels.append(count)

        return [len(pixels), pixels[-1]]

    def numberOfLines2(self, widths: List[int], s: str) -> List[int]:
        lines, width = 1, 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return [lines, width]


obj = Solution()
widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
          10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
s = "bbbcccdddaaa"
print(obj.numberOfLines2(widths, s))
