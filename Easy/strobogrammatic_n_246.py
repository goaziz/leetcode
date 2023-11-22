class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = ''

        for i in range(len(num)-1,  -1, -1):
            if num[i] in hashmap:
                res += hashmap.get(num[i])
            else:
                return False

        return num == res

    def isStrobogrammatic(self, num: str) -> bool:
        # two pointer approach
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left = 0
        right = len(num) - 1

        while left <= right:
            if num[left] not in hashmap or hashmap[num[left]] != num[right]:
                return False

            left += 1
            right -= 1
        
        return True


obj = Solution()
num = '1'
print(obj.isStrobogrammatic(num))
