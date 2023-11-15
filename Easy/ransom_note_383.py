from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        r = Counter(ransomNote)
        n = len(ransomNote)

        for char in ransomNote:
            m_value = m[char]
            r_value = r[char]

            if m_value >= r_value:
                n -= 1

        if n == 0:
            return True
        return False

    def canConstruct2(self, ransomNote, magazine):

        chars = {}
        for char in magazine:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

        for char in ransomNote:
            if char in chars and chars[char] > 0:
                chars[char] -= 1
            else:
                return False

        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        # pretty code. Not mine

        # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)

        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note:
            return True
        return False


obj = Solution()
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(obj.canConstruct(ransomNote, magazine))
