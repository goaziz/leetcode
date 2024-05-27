class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        ans = [count]
        current_char = s[0]

        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                current_char = char
                ans.append(count)
                count = 1

        ans.append(count)
        return max(ans)

    def maxPower2(self, s: str) -> int:
        count = 1
        max_count = 0
        current_char = s[0]

        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                current_char = char
                if count > max_count:
                    max_count = count
                count = 1

        if count > max_count:
            max_count = count

        return max_count

    def maxPower3(self, s: str) -> int:
        count = 0
        max_count = 0
        current_char = None

        for char in s:
            if char == current_char:
                count += 1
            else:
                current_char = char
                count = 1
            max_count = max(max_count, count)

        return max_count


obj = Solution()
s = "cc"
print(obj.maxPower2(s))
