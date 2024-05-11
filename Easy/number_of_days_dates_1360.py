import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        diff = (d2 - d1).days

        return diff if diff > 0 else diff * (-1)

    def daysBetweenDates2(self, date1: str, date2: str) -> int:

        def is_leap_year(year):
            """Check if a year is a leap year within the given range 1971-2100."""
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_in_month(month, year):
            """Return the number of days in a given month for the specific year range."""
            if month == 2:
                return 29 if is_leap_year(year) else 28
            elif month in [4, 6, 9, 11]:
                return 30
            else:
                return 31

        def days_from_1971(year, month, day):
            """Calculate total days from 1971 to the given date."""
            total_days = day
            for y in range(1971, year):
                total_days += 366 if is_leap_year(y) else 365
            for m in range(1, month):
                total_days += days_in_month(m, year)
            return total_days

        """Calculate the number of days between two dates within the range 1971 to 2100."""
        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))

        # Compute total days from 1971 for both dates and find the difference
        days1 = days_from_1971(year1, month1, day1)
        days2 = days_from_1971(year2, month2, day2)

        return abs(days2 - days1)


obj = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(obj.daysBetweenDates(date1, date2))
