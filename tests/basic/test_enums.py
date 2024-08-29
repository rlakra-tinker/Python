#
# Author: Rohtash Lakra
#
import unittest
from basic.enums import BaseEnum, ColorEnum, WeekDaysEnum
from datetime import date

# Unit-tests for constants
class EnumsTest(unittest.TestCase):
    """Unit-tests for Enums"""

    def test_base_enum(self):
        print("test_base_enum")

        self.assertEqual("<enum 'BaseEnum'>", str(BaseEnum))
        self.assertEqual((), BaseEnum.names())
        self.assertEqual((), BaseEnum.values())
        text = 'name'
        print(f"{text} of_name={BaseEnum.of_name(text)}")
        self.assertEqual(None, BaseEnum.of_name(text))
        print(f"{text} of_value={BaseEnum.of_value(text)}")
        self.assertEqual(None, BaseEnum.of_value(text))
        print(f"{text} equals={BaseEnum.equals(BaseEnum, text)}")
        self.assertEqual(False, BaseEnum.equals(BaseEnum, text))

    def test_color_enum(self):
        print("test_color_enum")
        self.assertEqual("<enum 'ColorEnum'>", str(ColorEnum))
        self.assertEqual(('RED', 'GREEN', 'BLUE'), ColorEnum.names())
        self.assertEqual((1, 2, 3), ColorEnum.values())

        text = 'color'
        print(f"{text} of_name={ColorEnum.of_name(text)}")
        self.assertEqual(None, ColorEnum.of_name(text))

        text = 1
        expected = 'ColorEnum <RED=1>'
        self.assertEqual(expected, str(ColorEnum.of_value(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.RED, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.GREEN, text))

        text = 'red'
        expected = 'ColorEnum <RED=1>'
        print(f"{text} of_name={WeekDaysEnum.of_name(text)}")
        self.assertEqual(expected, str(ColorEnum.of_name(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.RED, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.GREEN, text))

        text = 2
        expected = 'ColorEnum <GREEN=2>'
        print(f"{text} of_value={ColorEnum.of_value(text)}")
        self.assertEqual(expected, str(ColorEnum.of_value(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.GREEN, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.RGB, text))

        color = ColorEnum.RGB
        print(f"{color} is instance of {ColorEnum} = {isinstance(color, ColorEnum)}")
        self.assertTrue(isinstance(color, ColorEnum))

    def test_week_days_type(self):
        print("test_week_days_type")
        self.assertEqual("<enum 'WeekDaysEnum'>", str(WeekDaysEnum))
        self.assertEqual(('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'), WeekDaysEnum.names())
        self.assertEqual((1, 2, 3, 4, 5, 6, 7), WeekDaysEnum.values())
        text = 'sunday'
        expected = 'WeekDaysEnum <SUNDAY=1>'
        print(f"{text} of_name={WeekDaysEnum.of_name(text)}")
        self.assertEqual(expected, str(WeekDaysEnum.of_name(text)))
        self.assertTrue(WeekDaysEnum.equals(WeekDaysEnum.SUNDAY, text))
        self.assertFalse(WeekDaysEnum.equals(WeekDaysEnum.MONDAY, text))

        text = 2
        expected = 'WeekDaysEnum <MONDAY=2>'
        print(f"{text} of_value={WeekDaysEnum.of_value(text)}")
        self.assertEqual(expected, str(WeekDaysEnum.of_value(text)))
        self.assertTrue(WeekDaysEnum.equals(WeekDaysEnum.MONDAY, text))
        self.assertFalse(WeekDaysEnum.equals(WeekDaysEnum.SUNDAY, text))

        # check isinstance of
        week_day = WeekDaysEnum.WEEKEND
        print(f"{week_day} is instance of {WeekDaysEnum} = {isinstance(week_day, WeekDaysEnum)}")
        self.assertTrue(isinstance(week_day, WeekDaysEnum))

        # print weekday from date
        print(f"Weekday={WeekDaysEnum.fromDate(date.today())} for date:{date}. And today={WeekDaysEnum.today()}")
        print()

# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
