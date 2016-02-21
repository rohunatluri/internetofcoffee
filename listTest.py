from random import randint
from listCompiler import makeList

factlist = makeList(open("factlist.txt", "r"))

while True:
        num = randint(0, 15)
        fact = str(factlist[num])
        print fact