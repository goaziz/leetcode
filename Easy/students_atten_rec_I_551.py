class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0

        for char in s:
            if char == 'L':
                late_count += 1
            else:
                if late_count >= 3:
                    return False
                late_count = 0

            if char == 'A':
                absent_count += 1

            if absent_count >= 2 or late_count >= 3:
                return False

        return True

    def checkRecord2(self, s: str) -> bool:
        absent_count = 0

        for char in s:
            if char == 'A':
                absent_count += 1

        return absent_count < 2 and s.find('LLL') < 0


obj = Solution()
print(obj.checkRecord2('PPALLP'))
print(obj.checkRecord2('PPALLL'))
