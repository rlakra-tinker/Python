#
# Author: Rohtash Lakra
#
import unittest

from basic.data_types import full_name


# Unit-tests for DataTypes
class DataTypesTest(unittest.TestCase):
    """Unit-tests for DataTypes"""

    def test_full_name(self):
        print("test_full_name")
        # first, middle and last
        fullName = full_name("first", "last", "middle")
        print("fullName={}".format(fullName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        assert fullName == "First Middle Last"
        # first and last
        firstAndLastName = full_name("first", "last")
        print("firstAndLastName={}".format(firstAndLastName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert firstAndLastName == "First Last"
        # first only
        firstNameOnly = full_name("first", None)
        print("firstNameOnly={}".format(firstNameOnly))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert firstNameOnly == "First"
        # last only
        lastNameOnly = full_name(None, "last")
        print("lastNameOnly={}".format(lastNameOnly))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert lastNameOnly == "Last"
        # no name
        noName = full_name(None, None)
        print("noName={}".format(noName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert noName == None
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
