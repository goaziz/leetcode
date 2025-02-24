from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        freq = {}
        result = []

        for name in names:
            if name not in freq:
                freq[name] = 0
                result.append(name)
            else:
                k = freq[name] + 1
                new_name = f"{name}({k})"

                while new_name in freq:
                    k += 1
                    new_name = f"{name}({k})"

                freq[name] += 1
                freq[new_name] = 0
                result.append(new_name)

        return result


obj = Solution()
names = ["gta", "gta(1)", "gta", "avalon"]
print(obj.getFolderNames(names))
