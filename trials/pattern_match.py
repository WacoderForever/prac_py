import re

match=re.match('Hello[\t]*(.*) world','Hello    Python world')
m=match.group()
print(m)