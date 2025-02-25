from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed_transactions = []  # Store transactions in structured format
        invalid_transactions = set()  # Store invalid transactions
        hashmap = defaultdict(list)  # Store transactions by name

        # Step 1: Parse transactions and store them
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            parsed_transactions.append((name, time, amount, city, transaction))
            hashmap[name].append((time, amount, city, transaction))

            if amount > 1000:
                invalid_transactions.add(transaction)

        # Step 2: Check for transactions in different cities within 60 minutes
        for name, time, amount, city, transaction in parsed_transactions:
            for prev_time, prev_amount, prev_city, prev_transaction in hashmap[name]:
                if abs(time - prev_time) <= 60 and city != prev_city:
                    invalid_transactions.add(transaction)
                    invalid_transactions.add(prev_transaction)

        # Step 3: Return results in original order
        return [t for t in transactions if t in invalid_transactions]


obj = Solution()
transactions = ["alice,20,800,mtv", "bob,50,1200,mtv", "alice,20,800,mtv",
                "alice,50,1200,mtv", "alice,20,800,mtv", "alice,50,100,beijing"]
print(obj.invalidTransactions(transactions))
