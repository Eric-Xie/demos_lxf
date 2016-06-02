# -*- coding: utf-8 -*-

class Student(object):

    # def __init__(self, name, score):
    #     self.__name = name
    #     self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer.")
        if value < 0 or value > 100:
            raise ValueError("Score must between 0~100.")
        self.__score = value

class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height

def main():

    print("------Demo 1-----")
    s = Student()
    s.score = 60
    print(s.score)
    # s.score = 110

    print("------Demo 2-----")
    screen = Screen()
    screen.width = 1024
    screen.height = 768
    print(screen.resolution)
    assert screen.resolution == 786432, '1024 * 768 = %d ?' % screen.resolution

if __name__ == '__main__':
    main()