class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for p in path:
            if p == '...':
                stack.append('...')
            elif p == '..':
                if stack:
                    stack.pop()
            elif p != '' and p != '.':
                stack.append(p)

        return '/' + '/'.join(stack)


obj = Solution()
path = '/../'
print(obj.simplifyPath(path))
