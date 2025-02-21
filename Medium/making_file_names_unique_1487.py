from collections import Counter, defaultdict
import re
from typing import List


class Solution:

    def clean_name_and_get_number(self, name):
        cleaned_name = re.sub(r'\(\d+\)', '', name).strip()
        number = re.findall(r'\((\d+)\)', name)

        return cleaned_name, int(number[0]) if number else 0

    def getFolderNames(self, names: List[str]) -> List[str]:
        pass


obj = Solution()
names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
print(obj.getFolderNames(names))
