import re

p=re.compile('a*c*(bb)a*c*')
#print (p.match('a'))

print (p.match('aaaaaaaaaaaabbbbbbcccc'))
