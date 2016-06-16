# -*- coding: utf-8 -*-
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

def main():

    print("------Demo 1-----")
    Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    print("------Demo 2-----")
    day1 = Weekday.Sun
    print(day1, '=>', day1.value)
    for name, member in Weekday.__members__.items():
        print(name, '=>', member, ',', member.value)

    print("------Demo 3-----")

if __name__ == '__main__':
    main()