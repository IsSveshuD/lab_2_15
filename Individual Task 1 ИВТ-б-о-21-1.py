#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать программу, которая считывает английский текст из файла и
выводит на экранслова текста, начинающиеся и оканчивающиеся
на гласные буквы.
"""


if __name__ == "__main__":
    with open('test.txt') as file:
        numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять',
                   'шесть', 'семь', 'восемь', 'девять']
        string = file.read()
        for number in range(len(numbers)):
            string = string.replace(str(number), numbers[number]).replace(". ", ".\n")
        print(string)
