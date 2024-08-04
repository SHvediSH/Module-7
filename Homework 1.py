from pprint import pprint
name = 'SomeSample'
file = open(name, 'r')
pprint(file.read())
file.close()