


def isValid(s):

    stack = []
    hash_map = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in hash_map:
            elem = stack.pop() if stack else '#'
            print(elem)
            if hash_map[i] != elem:
                return False
        else:
            stack.append(i)
    return not stack

print(isValid('({})'))