import re

string1 = '''Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches1 = pattern.finditer(string1)

print(matches1)

count = 0
for match in matches1:
    print(match)
    count += 1

print(count)
# print(string1[450: 455])
