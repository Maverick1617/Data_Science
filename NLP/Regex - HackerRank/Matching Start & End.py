Regex_Pattern = r"^\d....\.$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
