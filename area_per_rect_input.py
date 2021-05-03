#!/usr/bin/env python3
# Created By: Layla Michel
# Date: May 3, 2021
# This program calculates the area and perimeter of a
# rectangle using values the user inputed.

def main():
    # get user input
    global length
    print("Hello we will calculate the area and perimeter of a rectangle!")
    length = float(input("Enter length of the rectangle (mm): "))
    width_input()


def width_input():
    # calculate the area and perimeter
    width = float(input("Enter width of the rectangle (mm): "))
    print("The area of the rectangle is: {} mm^2". format(length*width))
    print("The perimeter of the rectangle is: {} mm". format(2*(length+width)))


if __name__ == "__main__":
    main()
