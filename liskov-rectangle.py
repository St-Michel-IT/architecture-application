"""
This module aims to highlight the S.O.L.I.D. Liskov substitution principle.
The basic version does not follow the Liskov substitution principle, and
therefore it is to refactor.
"""


class Rectangle:
    """
    This class represents a rectangle.
    Its area is calculated by multiplying the width and height.
    """

    def __init__(self, width=0, height=0) -> None:
        """
        Constructor, initializes the width and height of the rectangle.

           :param width: Width of the rectangle, default is 0.
           :param height: Height of the rectangle, default is 0.
        """
        self.width = width
        self.height = height

    def set_width(self, width: int | float) -> None:
        """
        Set the width of the rectangle.

           :param width: An integer or a float value defining the width of the
              rectangle.
        """
        self.width = width

    def set_height(self, height: int | float) -> None:
        """
        Set the height of the rectangle.

           :param height: An integer or a float value defining the height of the
              rectangle.
        """
        self.height = height

    def get_area(self) -> int | float:
        """
        Calculate the area of the rectangle by multiplying the width and height.

           :return: An integer or a float depending on the height and width.
        """
        return self.width * self.height


class Square(Rectangle):
    """
    A square having all its sides equal.
    """

    def __init__(self, side=0):
        """
        Constructor initializing the side of the square.

           :param side: An integer or a float, default is 0.
        """
        super().__init__()
        self.side = side

    def set_side(self, side: int | float):
        """
        Set the side of the square.

           :param side:
        """
        self.side = side

    def get_area(self) -> int | float:
        return self.side ** 2


def check_shape_area(shape: Rectangle | Square):
    """
    This function should work for both Rectangle and Square.
    
       :param shape: A Rectangle or a Square object.
       :raise AssertionError: If the area is not calculated correctly. 
    """
    height = 10
    shape.set_height(height)
    w = shape.width
    assert shape.get_area() == w * height


rc = Rectangle(2, 3)
check_shape_area(rc)

sq = Square(5)
check_shape_area(sq)
