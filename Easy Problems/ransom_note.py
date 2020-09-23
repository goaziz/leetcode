
from collections import Counter

def canConstruct(ransomNote, magazine):
    return not Counter(ransomNote) - Counter(magazine)

r = "bg"
m = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print(canConstruct(r, m))


