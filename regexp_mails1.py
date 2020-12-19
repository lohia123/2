import re

emails = '''CoreyMScafer@gmail.com
corey.schaferr@university.edu
corey-321-schafer@my-work.net
'''


pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.[a-z]+')

matches1 = pattern.finditer(emails)

print(matches1)

count = 0
for match in matches1:
    print(match)
    count += 1

print(count)
# print(string1[450: 455])
