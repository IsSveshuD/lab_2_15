#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать программу, которая считывает текст из файла и выводит его на экран,
заменив цифры от 0 до 9 на слова «ноль», «один», ..., «девять», начиная
каждое предложение с новой строки.
"""


if __name__ == "__main__":
    with open('test.txt') as file:
        numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять',
                   'шесть', 'семь', 'восемь', 'девять']
        string = file.read()
    string = string.replace('. ', '.\n')
    end = ''
    for number in string:
        if number.isnumeric():
            number = numbers[int(number)]
        end += number
    print(end)
