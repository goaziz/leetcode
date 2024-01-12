class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s + s and len(s) == len(goal)

    def rotateString2(self, s: str, goal: str) -> bool:
        if s != goal:
            return False

        s, goal = [*s], [*goal]

        # unpacking the strings (creates list)
        # ex: 'hello' -> ['h','e','l','l','o']

        for x in range(len(s)):
            a = s[0]
            s.pop(0)
            s.append(a)
            
            if s == goal:
                return True

        return False


obj = Solution()
s = 'abcde'
goal = 'abced'
print(obj.rotateString2(s, goal))
