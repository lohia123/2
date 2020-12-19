import re

urls = '''Https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'[a-z.:/]+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# pattern = re.compile(r'(https?://)(www)?(\.?)(\w+)(\.\w+)')
# pattern = re.compile(r'\w+://\w+\.\w+\.\w+')
# pattern = re.compile(r'[a-z.:/]+')
pattern = re.compile(r'https', re.IGNORECASE)

# matches = pattern.finditer(urls)
# matches = pattern.findall(urls)
# matches = pattern.match(urls)
matches = pattern.search(urls)

# count = 0
# for match in matches:
#     print(match)
#     count += 1

# print(count)
print(matches)
