class Solution:
    def interpret(self, command: str) -> str:
        res = ""

        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(' and command[i + 1] == 'a':
                res += 'al'
            elif command[i] == '(' and command[i + 1] == ')':
                res += 'o'

        return res

    def interpret2(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


obj = Solution()
command = "(al)G(al)()()G"
print(obj.interpret(command))
