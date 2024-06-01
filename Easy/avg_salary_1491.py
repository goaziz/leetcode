from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        max_salary = max(salary)
        min_salary = min(salary)
        s = sum(salary) - min_salary - max_salary

        return s / (n - 2)


obj = Solution()
salary = [4000, 3000, 1000, 2000]
print(obj.average(salary))
