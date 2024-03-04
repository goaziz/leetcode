class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month] + bool(month == 2 and (year % 4 == 0 and (year % 100 or year % 400 == 0)))

    def dayOfYear(self, date: str) -> int:
        res = 0
        year, month, day = map(int, date.split('-'))

        if month == 1:
            return day

        for i in range(1, month):
            days = self.numberOfDays(year, i)
            res += days

        res += day

        return res


obj = Solution()
date = "2019-02-10"
print(obj.dayOfYear(date))
