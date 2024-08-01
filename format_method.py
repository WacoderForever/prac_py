import sys
k={'kind':'laptop','platform':sys.platform,'cost':120000000000}
r='My {kind} runs {platform} it cost me ${cost:,d}'.format(**k)
print(r)