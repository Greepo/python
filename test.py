#! python
from random import Random, randint, random
from tkinter.tix import INTEGER


class Losowanie:
    def __init__(self, numer, date, numbers):
        self.numer = numer
        self.date = date
        self.numbers = numbers
x=0
file = open('dl.txt', 'r')
Lines = file.readlines()
loses = []


for line in Lines:
    pices = line.split(' ')
    x=x+1
    #loses = Losowanie(pices[0], pices[1], pices[2])
    loses.append(Losowanie(pices[0], pices[1], pices[2]))
    

print(loses[randint(0,x)].numbers)

        
