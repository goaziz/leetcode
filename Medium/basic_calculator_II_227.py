class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        stack = []
        operator = '+'
        num = 0
        print(len(s))

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '/*+-' or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    stack.append(int(stack.pop() / num))

                operator = char
                num = 0

        return sum(stack)

    def calculate2(self, s: str) -> int:
        s = s.strip()
        res = 0
        current_num = 0
        last_num = 0
        oper = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            if char in '+/*-' or i == len(s) - 1:
                if oper == '+' or oper == '-':
                    res += last_num
                    last_num = current_num if oper == '+' else -current_num
                elif oper == '*':
                    last_num = last_num * current_num
                elif oper == '/':
                    last_num = int(last_num / current_num)

                oper = char
                current_num = 0

        return res + last_num


obj = Solution()
s = " 3+5 / 2 "
print(obj.calculate2(s))
