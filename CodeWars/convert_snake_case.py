import re

def to_underscore(string):
    try:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    except:
        return str(string)
st = 1
print(to_underscore(st))