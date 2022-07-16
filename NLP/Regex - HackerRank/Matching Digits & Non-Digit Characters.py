
Regex_Pattern = r'[0-9]{2}\D[0-9]{2}\D\d{4}'


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
