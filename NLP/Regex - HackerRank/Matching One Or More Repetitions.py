Regex_Pattern = r"^\d+[A-Z]+[a-z]+$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
