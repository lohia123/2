import re

string1 = '''Regular expressions , or regexes for short, are a way to match text with patterns.
            Since regexes are language Since independent, we're Since trying to keep this Since article as language
            independent as possible. However, it's to be noted that not all regex implementations are the same.
            The below text is based on Perl 5.0 Since Since Since Since.
            123456789
            !@#$%^&*()_+|:"<>?~
            lohia.com
            213-456-987
            Mr. lohia
            Mr lohia
            lohia lohiasaroja
            LOHIA LOHIA'''

pattern = 'Since'

matches1 = re.finditer(pattern, string1)
print(matches1)
for match in matches1:
    print(match)

