import math


class Shape:
    def __init__(self, x_position: (int | float), y_position: (int | float)):
        self.x_position = x_position
        self.y_position = y_position

    def __repr__(self) -> str:
        return f"{self.x_position},{self.y_position}"

    def __str__(self) -> str:
        return f"The shapes x-position is {self.x_position} and its y-position is {self.y_position}"

    # -------------------- Getters/setters (Shape) --------------------
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

    # -------------------- Overloading operators --------------------

    def __eq__(self, other) -> bool:
        return self.area == other.area

    def __lt__(self, other) -> bool:
        return self.area < other.area

    def __gt__(self, other) -> bool:
        return self.area > other.area

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area

    # -------------------- translation method --------------------

    def translate(self, x_value: (int | float), y_value: (int | float)):
        if not isinstance(x_value, (int, float)):
            raise TypeError(f"x value has to be either int or float, not {type(x_value)}")
        self.x_position = x_value

        if not isinstance(y_value, (int, float)):
            raise TypeError(f"y value has to be either int or float, not {type(y_value)}")
        self.y_position = y_value


class Circle(Shape):
    def __init__(self, x_position: int | float, y_position: int | float, radius: int | float):
        super().__init__(x_position, y_position)
        self.radius = radius

    def __repr__(self) -> str:
        return f"{self.x_position},{self.y_position},{self.radius}"

    def __str__(self) -> str:
        return (f"The shapes x-position is {self.x_position}, "
                f"its y-position is {self.y_position} and the radius is {self.radius}")

    # -------------------- Getters/setters (Circle) --------------------

    @property
    def radius(self) -> int | float:
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Value has to be either int or float, not {type(value)}")
        if value <= 0:
            raise ValueError(f"Value has to be positive, not {value}")
        self._radius = value

    @property
    def area(self) -> int | float:
        return math.pi * self.radius ** 2

    @property
    def circumference(self) -> (int | float):
        return 2 * math.pi * self.radius

    # -------------------- Methods (Circle) --------------------

    def is_unit_circle(self) -> bool:
        return self.radius == 1 and self.x_position == 0 and self.y_position == 0

    def is_inside_circle(self, x: int | float, y: int | float) -> bool:
        if not isinstance(x, (int, float)):
            raise TypeError(f"x value has to be either int or float, not {type(x)}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y value has to be either int or float, not {type(y)}")
        return (x - self.x_position) ** 2 + (y - self.y_position) ** 2 < self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x_position: int | float, y_position: int | float, width: int | float, height: int | float):
        super().__init__(x_position, y_position)
        self.width = width
        self.height = height

    # -------------------- Getters/setters (Rectangle) --------------------

    @property
    def width(self) -> (int | float):
        return self._width

    @width.setter
    def width(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value has to be either int or float, not {type(value)}")
        if value <= 0:
            raise ValueError(f"Value has to be positive, not {value}")
        self._width = value

    @property
    def height(self) -> (int | float):
        return self._height

    @height.setter
    def height(self, value: int | float):
        if not isinstance(value, (int | float)):
            raise TypeError(f"Value has to be either int or float, not {type(value)}")
        if value <= 0:
            raise ValueError(f"Value has to be positive, not {value}")
        self._height = value

    @property
    def area(self) -> (int | float):
        return self.width * self.height

    @property
    def circumference(self) -> (int | float):
        return (self.width + self.height) * 2
