class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        result = float('inf')
        valid_ends = ["00", "25", "50", "75"]

        # Check for a valid last two-digit number
        for d2 in range(n - 1, -1, -1):  # Last digit position
            for d1 in range(d2 - 1, -1, -1):  # Second-last digit position
                last_two = num[d1] + num[d2]

                if last_two in valid_ends:
                    deletions = (d2 - d1 - 1) + (n - d2 - 1)
                    result = min(result, deletions)

        # If no valid two-digit number, check for a single '0'
        if result == float('inf'):
            return n - 1 if '0' in num else n  # If '0' exists, delete everything except '0'

        return result


obj = Solution()
num = "2908305"
print(obj.minimumOperations(num))
