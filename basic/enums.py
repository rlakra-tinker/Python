# Python Enums
# Author: Rohtash Lakra
# Reference - https://docs.python.org/3/howto/enum.html
#
from enum import Enum, auto, unique

# Define Colors Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    RGB = 3

# Print Color Enum
print()
print(Color)
print(Color.RGB)
print(type(Color.RGB))
colors = list(Color)
print(colors)
print()


# Define Weekday Enum
class WeekDay(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
    WEEKEND = SATURDAY | SUNDAY

    # add a method to return the weekday from the date
    # @param date
    @classmethod
    def fromDate(cls, date):
        return cls(date.isoweekday())

    # add a method to return the today's weekday.
    @classmethod
    def today(cls):
        return WeekDay.fromDate(date.today())


# Print WeekDay Enum
print()
print(WeekDay)
print(WeekDay.WEEKEND)
print(type(WeekDay.WEEKEND))
weekDays = list(WeekDay)
print(weekDays)
print()

# Check is_instance
color = Color.RGB
print(f"{color} color is instance of {Color} = {isinstance(color, Color)}")
print(f"Color <name={color.name}, value={color.value}>")
weekDay = WeekDay.WEDNESDAY
print(f"The {color} is instance of {WeekDay} = {isinstance(color, WeekDay)}")
print(f"Color <name={weekDay.name}, value={weekDay.value}>")
print()

# print weekday from date
from datetime import date
print(f"Weekday={WeekDay.fromDate(date.today())} for date:{date}. And today={WeekDay.today()}")
print()


# In cases where the actual values of the members do not matter,
# you can save yourself some work and use auto() for the values:
class Number(Enum):
    EVEN = auto()
    ODD = auto()
    PRIME = auto()

print()
num = Number.EVEN
print(num)
numbers = list(Number)
print(numbers)
print()

# Duplicating enum members and values
class Shape(Enum):
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3
    DIAMOND_ALIAS = 2

    @classmethod
    def allShapes(cls):
        # return cls(list(Shape.__members__.items()))
        # returns (name, Enum) as list
        return list(Shape.__members__.items())


print()
# shapes = [f"{entry.name} = {entry.value}" for entry in Shape]
shapes = []
for entry in Shape:
    shapes.append(f"{entry.name} = {entry.value}")
# shapes = list([f"{entry.name} = {entry.value}" for entry in Shape])
print(shapes)
shape = Shape.DIAMOND
print(shape)
shape = Shape.DIAMOND_ALIAS
print(shape)
# Iterating over the members of an enum does not provide the aliases:
shapes = list(Shape)
print(shapes)
print()

# Note that the aliases Shape.DIAMOND_ALIAS and WeekDay.WEEKEND aren’t shown.
# The special 'attribute __members__' is a read-only ordered mapping of names to members.
# It includes all names defined in the enumeration, including the aliases:
# allShapes = list([name, entry for name, entry in Shape.__members__().items()])
print("Print all members including aliases:")
for name, shape in Shape.__members__.items():
    print(f"{name}, {shape}")

print()
# The special attribute __members__ is a read-only ordered mapping of names to members.
# It includes all names defined in the enumeration, including the aliases:
print("Print all Enums:")
print(Shape.allShapes())
print()

# Ensuring unique enumeration values
@unique
class UniqueShape(Enum):
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3

shapeUnique = UniqueShape.DIAMOND
print(shapeUnique)
uniqueShapes = list(UniqueShape)
print(uniqueShapes)
print()


# Using automatic values
class Status(Enum):

    # The values are chosen by _generate_next_value_() static, which can be overridden:
    # Note The _generate_next_value_() method must be defined before any members.
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ENABLED = auto()
    DISABLED = auto()
    MODIFIED = auto()
    DELETED = auto()

    """
    _missing_(cls, value)
    A classmethod for looking up values not found in cls. 
    By default it does nothing, but can be overridden to implement custom search behavior:
    """
    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member

        return None


print()
statuses = list(Status)
print(f"statuses={statuses}")
print()

# # Print Status
# for entry in Status:
#     print(f"{entry.name} = {entry.value}")


# Also, subclassing an enumeration is allowed only if the enumeration does not define any members.
# Auto name for the enum members
class AutoName(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name

# Auto lowercase name
class AutoNameLowerCase(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

# Ordinal Enum
class Ordinal(AutoName):
    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST =  auto()

print()
ordinals = list(Ordinal)
print(f"ordinals={ordinals}")
print()

# LowerCase Ordinal Enum
class LowerCaseOrdinal(AutoNameLowerCase):
    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST =  auto()

print()
lowerCaseOrdinals = list(LowerCaseOrdinal)
print(f"lowerCaseOrdinals={lowerCaseOrdinals}")
print()

# Enumeration members are compared by identity:
print()
status = Status.ENABLED
print(f"status={status} is enabled:{status is Status.ENABLED}")
print(f"status={status} is disabled:{status is Status.DISABLED}")
print(f"status={status} is enabled:{status == 'Status.ENABLED'}")
print(f"status={status} is enabled:{status.value == 'Status.ENABLED'}")
print(f"Length of {Status} is {len(Status)}")
print(f"Reversed {Status} are: {list(reversed(Status))}")
print()
camelCaseEnabled = 'eNableD'
print(f"{camelCaseEnabled} equals to {Status(camelCaseEnabled)}")
print()

from enum import IntEnum, IntFlag

class EvenOdd(IntFlag):
    EVEN = auto()
    ODD = auto()

print()
print("EvenOdd")
evenAndOdds = list(EvenOdd)
print(f"evenAndOdds={evenAndOdds}")
print()

class LogType(IntEnum):
    ALL = auto()
    DEBUG = auto()
    INFO = auto()
    WARN = auto()
    ERROR = auto()

print()
print("LogType")
logTypes = list(LogType)
print(f"logTypes={logTypes}")
# assert LogType.INFO == "INFO"
print()

import sys

print()
print("Sys Version: {sys.version_info}")
print()
# String Enum
if sys.version_info >= (3, 11):
    from enum import StrEnum
    # from strenum import StrEnum
    class HttpMethod(StrEnum):
        GET = auto()
        HEAD = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        CONNECT = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()
else:
    @unique
    class HttpMethod(AutoName):
        CONNECT = auto()
        HEAD = auto()
        GET = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()

        """
        _missing_(cls, value)
        A classmethod for looking up values not found in cls. 
        By default it does nothing, but can be overridden to implement custom search behavior:
        """
        @classmethod
        def _missing_(cls, value):
            value = value.upper()
            for member in cls:
                if member.value == value:
                    return member

            return None

print()
print("HttpMethod")
httpMethods = list(HttpMethod)
print(httpMethods)
print()
httpMethod = 'Get'
print(f"{httpMethod} equals to {HttpMethod(httpMethod)}")
print()