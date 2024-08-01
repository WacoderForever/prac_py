import sys

data={'angel':'Gabriel','devil':'Lucifer'}
print('My {map[machine]} runs {sys.platform} {map[time]}'.format(sys=sys,map={'machine':'laptop','time':'everyday'}))
print('{angel} defeated {devil} after '.format(**data),end='')
print('{0:,d} fights'.format(99999999999999))