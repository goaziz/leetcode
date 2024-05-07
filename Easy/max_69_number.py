class Solution:
    def maximum69Number(self, num: int) -> int:
        l = [num]
        nums = [int(n) for n in str(num)]

        for i in range(len(nums)):
            temp = nums[:]
            if nums[i] == 9:
                temp[i] = 6
            else:
                temp[i] = 9
            n = int(''.join(map(str, temp)))
            l.append(int(n))

        return max(l)

    def maximum69Number2(self, num: int) -> int:
        num_char_list = list(str(num))
        
        for i, cur_char in enumerate(num_char_list):
            if cur_char == '6':
                num_char_list[i] = '9'
                break
            
        return int("".join(num_char_list))

    def maximum69Number3(self, num: int) -> int:
        s = str(num)
        return int(s.replace('6', '9', 1))

obj = Solution()
num = 9669
print(obj.maximum69Number2(num))
