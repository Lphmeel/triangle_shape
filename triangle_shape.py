#!/usr/bin/env python
"""
SYNOPSIS

    triangle_shape.py
    This script has no command line arguments required to run.
DESCRIPTION

    Enter three inputs for the three sides of the triangle.

EXAMPLES

    User enters the first value 4.
    User enters the second value 5.
    User enters the third value 6.
    The output gives that the triangle is Scalene.

AUTHOR

    Dyn Candido <p276126@tafe.wa.edu.au>

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

1.0
"""
# Scenario 1 code
# value1 holds the first input value
value1 = float(input('Enter first value: '))
# value2 holds the second input value
value2 = float(input('Enter second value: '))
# value3 holds the third input value
value3 = float(input('Enter third value: '))

# determines all three values are equal to each other and outputs the
# triangle is an equilateral shape
if value1 == value2 and value2 == value3 and value3 == value1:
    print('The triangle is Equilateral.')

# determines either two of the values are equal to each other and outputs the
# triangle is an isosceles shape
elif value1 == value3 and value1 != value2 or value1 == value2 and value1 != value3 or value3 == value2 and value3 != value1:
    print('The triangle is Isosceles.')

# determines neither three values are equal to each other and outputs the
# triangle is a scalene shape
elif value1 != value3 and value1 != value2 and value2 != value3:
    print('The triangle is Scalene.')
