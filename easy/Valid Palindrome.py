import re

s = "A man, a plan, a canal: Panama"
s = "0P"

trim = re.sub(r'[^a-z]+', "", s.lower())

print(trim[::-1], trim)