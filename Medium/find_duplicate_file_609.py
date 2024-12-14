from collections import defaultdict
from typing import List, Dict


class Solution:

    def countFreq(self, path: List[str], hashmap: Dict[str, list]) -> Dict[str, list]:
        for p in path[1:]:
            file = p.split('.')
            content = file[1][4:-1]
            corrected_path = '{}/{}.txt'.format(path[0], file[0])
            hashmap[content].append(corrected_path)

        return hashmap

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for path in paths:
            hashmap = self.countFreq(path.split(), hashmap)

        answer = []
        for val in hashmap.values():
            if len(val) > 1:
                answer.append(val)

        return answer

    def findDuplicate2(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_entry in parts[1:]:
                file_name, content = file_entry.split('(')
                content = content[:-1]
                full_path = '{}/{}'.format(directory, file_name)
                hashmap[content].append(full_path)

        return [files for files in hashmap.values() if len(files) > 1]


obj = Solution()
paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
         "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]
print(obj.findDuplicate2(paths))
