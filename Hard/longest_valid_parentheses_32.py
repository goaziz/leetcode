class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        valid = [0] * len(s)

        # Mark valid pairs in the valid array
        for i, char in enumerate(s):
            if char == ')' and stack and s[stack[-1]] == '(':
                opening_index = stack.pop()
                valid[i] = 1
                valid[opening_index] = 1
            else:
                stack.append(i)

        # Find the longest streak of 1s
        max_length = current = 0
        for v in valid:
            if v == 1:
                current += 1
                max_length = max(max_length, current)
            else:
                current = 0

        return max_length

    def longestValidParentheses2(self, s: str) -> int:
        stack = []
        max_len = 0
        last_invalid = -1  # Position before the start of current valid substring

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                if stack:
                    stack.pop()
                    if stack:
                        # Valid substring is between current index and last unmatched '('
                        max_len = max(max_len, i - stack[-1])
                    else:
                        # All opened are matched, so valid from last_invalid + 1 to i
                        max_len = max(max_len, i - last_invalid)
                else:
                    # This ')' is unmatched; mark as last invalid position
                    last_invalid = i

        return max_len


obj = Solution()
s = ")(((((()())()()))()(()))("
print(obj.longestValidParentheses2(s))
