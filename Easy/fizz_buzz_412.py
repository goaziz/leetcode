from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for i in range(1, n + 1):
            res = str(i)
            if i % 3 == 0 and i % 5 == 0:
                res = "FizzBuzz"
            elif i % 3 == 0:
                res = "Fizz"
            elif i % 5 == 0:
                res = "Buzz"

            output.append(res)

        return output
    
    def fizzBuzz2(self, n: int) -> List[str]:
        hashmap = {3: 'Fizz', 5: 'Buzz'}
        divisors = [3, 5]
        output = []
        
        for i in range(1, n+1):
            num_ans_str = []
            
            for key in divisors:
                if i % key == 0:
                    num_ans_str.append(hashmap[key])
            
            if not num_ans_str:
                num_ans_str.append(str(i))
            
            output.append(''.join(num_ans_str))
        
        return output
            
        


obj = Solution()
n = 15
print(obj.fizzBuzz2(n))
