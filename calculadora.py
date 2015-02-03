#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    print
    sys.exit("Usage: calculadora.py num1 operand num2")

num1 = sys.argv[1]
operand = sys.argv[2]
num2 = sys.argv[3]


def sum(num1, num2):
    return float(num1) + float(num2)


def diff(num1, num2):
    return float(num1) - float(num2)


def mult(num1, num2):
    return float(num1) * float(num2)


def div(num1, num2):
    return float(num1) / float(num2)


if __name__ == "__main__":
    try:
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
    except ValueError:
            print "Please, enter two numbers"
    except ZeroDivisionError:
            print "Error: divide by zero"
