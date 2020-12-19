import re

urls = '''https://wwww.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'[a-z.:/]+')

matches = pattern.finditer(urls)

count = 0
for match in matches:
    print(match)
    count += 1

print(count)
