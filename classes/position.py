#!/usr/bin/python3

class Position:
    """Class was designed a position by:
        - his "x" array
        - gis "y" array
    """
    def __init__(self, x, y):
        """constructor of class Position"""
        self.x = x#x array
        self.y = y#y array


def main():
    position = Position(10, 10)
    print("position: x:{}, y:{}".format(position.x, position.y))


if __name__ == "__main__":
    main()
