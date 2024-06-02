class Solution:
    def reformatDate(self, date: str) -> str:
        splitted_date = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        year = splitted_date[2]
        month = months.index(splitted_date[1]) + 1
        day = splitted_date[0][:-2]

        if month < 10:
            month = f'0{month}'

        if len(day) < 2:
            day = f'0{day}'

        return f'{year}-{month}-{day}'


obj = Solution()
date = "6th Jun 1933"
print(obj.reformatDate(date))
