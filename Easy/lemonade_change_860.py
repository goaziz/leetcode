from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] in [10, 20]:
            return False

        change = {}

        for bill in bills:
            if bill == 5:
                change[bill] = change.get(bill, 0) + 1
            elif bill == 10:
                if change.get(5, 0) > 0:
                    change[bill] = change.get(bill, 0) + 1
                    change[5] = change.get(5) - 1
                else:
                    return False
            else:
                if change.get(5, 0) > 0:
                    if change.get(10, 0) > 0:
                        change[5] = change.get(5) - 1
                        change[10] = change.get(10) - 1
                    elif change.get(5, 0) > 2:
                        change[5] = change.get(5) - 3
                    else:
                        return False
                else:
                    return False

        return True

    def lemonadeChange2(self, bills: List[int]) -> bool:
        if bills[0] in [10, 20]:
            return False

        five_bills = []
        ten_bills = []

        for bill in bills:
            if bill == 5:
                five_bills.append(bill)
            elif bill == 10:
                if len(five_bills) > 0:
                    ten_bills.append(bill)
                    five_bills.pop()
                else:
                    return False
            else:
                if len(ten_bills) > 0 and len(five_bills) > 0:
                    ten_bills.pop()
                    five_bills.pop()
                elif len(five_bills) > 2:
                    ten_bills.pop()
                    ten_bills.pop()
                else:
                    return False

        return True

    def lemonadeChange3(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                ten += 1
                five -= 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


obj = Solution()
bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
print(obj.lemonadeChange3(bills))
