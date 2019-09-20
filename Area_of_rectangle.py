#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This proogram calculates perimeter and area of a rectangle
# with dimensions 5cm and 3cm


def main():
    # This function calculates area

    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = length*width

    # output
    print("")
    print("Area is {}mm^2".format(area))


if __name__ == "__main__":
    main()
