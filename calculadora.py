#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def sum(num1, num2):
    return num1 + num2


def diff(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        resul = num1 / num2
    except:
        print "Error: divide by zero"
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print
        sys.exit("Usage: calculadora.py num1 operand num2")
    operand = sys.argv[2]

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[3])
    except ValueError:
        print "Please, enter two numbers"

    if operand == "+":
        print str(sum(num1, num2))
    elif operand == "-":
        print str(diff(num1, num2))
    elif operand == "x":
        print str(mult(num1, num2))
    elif operand == "/":
        print str(div(num1, num2))
    else:
        print "Operations available: + - x /"
        sys.exit()
