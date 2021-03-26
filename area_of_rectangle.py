#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys
# import pdb; pdb.set_trace()

height = float(sys.argv[1])
width = float(sys.argv[2|)

def area_of_rectangle(height, width = None):
    """
    Returns the area of a rectangle.

    Parameters
    ----------
    height : int or float 
        The height of the rectangle.
    width : int or float
        The width of the rectangle. If `None` width is assumed to be equal to 
        the height.

    Returns
    -------
    int or float
        The area of the rectangle

    Examples
    --------
    >>> area_of_rectangle(7)
    49
    >>> area_of_rectangle (7, 2)
    14
    """
    
    if (len(sys.argv)==2)):
        area = 2 * height
        return area

    if(len(sys.argv) == 2)):
        area = height * width
        return area
    
    if (len(sys.argv) <2) or (len(sys.argv) >3):
        message = (
                "{script_name}: Expecting one or two command-line arguments:\n"
                "\tthe height of a square or the height and width of a "
                "rectangle".format(script_name = sys.argv[0]))
        sys.exit(message)

if __name__ == '__main__':
    area = area_rectangle(height, width)
    message  = ("The area of a {h} X {w} rectangle is {a}".format(h=sys.argv[1], w=sys.argv[2], a=area))
    print(message)
