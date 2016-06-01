# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

class Animal(object):

    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

def main():

    print("------Demo 1-----")
    foo = Student('Bar', 89)
    foo.print_score()

    print("------Demo 2-----")
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())

    print("------Demo 3-----")

if __name__ == '__main__':
    main()