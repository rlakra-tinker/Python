#
# Author: Rohtash Lakra
#
import unittest
from basic.utils import Utils, JsonUtils

# Unit-tests for constants
class UtilsTest(unittest.TestCase):
    """Unit-tests for Enums"""

    def test_utils(self):
        print("test_utils")
        print(list(Utils))

    def test_print_args(self):
        print("test_print_args")
        print("print args")
        print(Utils.print_args('Hi', 'Rohtash', 2024, True))
        print()

    def test_print_kwargs(self):
        print("test_print_kwargs")
        print("print keyword args")
        print(Utils.print_kwargs(firstName='Rohtash', lastName='Lakra', age=21))
        print()

    def test_generate_uuid(self):
        print("test_print_kwargs")
        print("Generating UUID:")
        print(Utils.generate_uuid())

    def test_ensure_valid_dictionary(self):
        print("test_ensure_valid_dictionary")
        self.assertEqual("<enum 'JsonUtils'>", str(JsonUtils))

        text = '{}'
        json_data = JsonUtils.ensure_valid_dictionary(text)
        print(f"{text} json_data={json_data}")
        self.assertEqual({}, json_data)

        text = '{"name":"name"}'
        json_data = JsonUtils.ensure_valid_dictionary(text)
        print(json_data)
        print(f"{text} json_data={json_data}")
        self.assertEqual("name", json_data['name'])

# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
