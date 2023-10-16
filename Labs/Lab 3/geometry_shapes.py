class Shape:
    def __init__(self, x_position: (int | float), y_position: (int | float)):
        self.x_position = x_position
        self.y_position = y_position

    def __repr__(self) -> str:
        return f"x = {self.x_position}, y = {self.y_position}"

    def __str__(self) -> str:
        return f"The shapes x-position is {self.x_position} and its y-position is {self.y_position}"

    @property
    def x_position(self) -> int | float:
        return self._x_position

    @x_position.setter
    def x_position(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"x position has to be either int or float, not {type(value)}")
        self._x_position = value

    @property
    def y_position(self) -> int | float:
        return self._y_position

    @y_position.setter
    def y_position(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"y position has to be either int or float, not {type(value)}")
        self._y_position = value


class Circle(Shape):
    ...


class Rectangle(Shape):
    ...
