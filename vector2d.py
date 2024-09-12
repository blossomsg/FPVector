"""
This is a vector2d module.
"""
import math
from array import array


class Vector2d:
    """This class display's vector values using special methods.

    Examples:
        v1 = Vector(2, 5)
        v2 = Vector(5, 9)
        print(repr(v1))
        print(abs(v1))
        print(bool(v1))
        print(v1+v2)
        print(v1*5)
        print(type(v1.x), v1.y)
        print(format(v1, '.2f'))
        print(format(v1, '.3e'))
        print(bytes(v1))

        v1 = Vector2d(2, 5)
        v2 = Vector2d(2, 5)
        print(v1.__eq__(v2))

        print(format(v1, "p"))
        print(format(v1, ".3ep"))
        print(format(v1, "0.5fp"))
    """

    __match_args__ = ('x', 'y')
    typecode = "d"

    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2d(x, y)

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def __format__(self, format_spec):
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

v1 = Vector2d(1, 1)
v2 = Vector2d(2, 5)
print(hash(v1), hash(v2))