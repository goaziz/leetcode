class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        temp = s + s
        return goal in temp


obj = Solution()
s = 'abcde'
goal = 'abced'
print(obj.rotateString(s, goal))
