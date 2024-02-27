class Solution:

    def is_leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def numberOfDays(self, year: int, month: int) -> int:
        months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if self.is_leap_year(year) and month == 2:
            return 29
        else:
            return months.get(month)

    def numberOfDays2(self, year: int, month: int) -> int:
        return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month] + bool(month == 2 and (year % 4 == 0 and (year % 100 or year % 400 == 0)))


obj = Solution()
year = 2000
month = 2
print(obj.numberOfDays(year, month))
