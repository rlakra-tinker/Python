"""Implements ThreadPoolExecutor."""

__author__ = 'Rohtash Lakra (work.lakra@gmail.com)'

import uuid
from enum import Enum
from enums import HttpMethod
import json
from typing import Callable, TypeVar, List, Dict, Iterator

# These type variables are used by the container types.
_K = TypeVar('K') # Key type
_V = TypeVar('V') # Value type

class Utils(Enum):

    """
    Prints Arguments

    @:param args - tuple of positional arguments

    *args - collects additional positional arguments into a tuple, not a list. The arguments are accessible using tuple indexing and iteration.
    """

    @staticmethod
    def print_args(*args):
        for arg in args:
            print(arg)
        # for count, arg in enumerate(args):
        # print('{0}. {1}'.format(count, arg))

    """
    Prints Keyword Arguments
    
    @:param kwargs - dictionary of keyword arguments (keyword arguments (**kwargs) to a function)
    """

    @staticmethod
    def print_kwargs(**kwargs):
        # print(f"kwargs={kwargs}")
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))
            # print('{0} = {1}'.format(key, value))

    """
    Generates Unique UUID
    """

    @classmethod
    def generate_uuid(cls):
        return uuid.uuid4().hex

    """
    Parses User-Agent
    """

    @classmethod
    def parse_user_agent(cls, user_agent_str):
        translator = str.maketrans('', '', '{}\"')
        user_agent = user_agent_str.translate(translator)
        # print(f"user-agent:{user_agent}")

        # break the user-agent into tokens and build dictionary of key/value pair and return it.
        return {
            key.strip(): value.strip() if not value.isnumeric() else int(value.strip())
            for key, value in (token.split(':') for token in user_agent.split(',') if len(token.split(':')) == 2)
        }

    """
    Executes an HTTP Request
    """

    @staticmethod
    def execute(url, method=None):
        import urllib.request
        import ssl
        ssl.get_default_verify_paths()

        # validate the url is provided
        if len(url) == 0:
            raise ValueError("The <url> must provide!")

        # check the method provided
        if method is None:
            method = HttpMethod.GET

        result = None
        try:
            req = urllib.request.Request(url, method)
            with urllib.request.urlopen(req, context=ssl.create_default_context()) as response:
                result = response.read()
        except Exception as ex:
            print(ex)
            raise ex

        return result

    @staticmethod
    def group_by(items: Iterator[_V],
                 *,
                 key: Callable[[_V], _K],
                 ) -> Dict[_K, List[_V]]:
        """Groups items based on whether they produce the same key from a function.

        Args:
            items: The items to group.
            key: Items that produce the same value from this function get grouped together.

        Returns:
            A dictionary mapping outputs that were produced by the grouping function to
            the list of items that produced that output.

        Examples:
            >>> group_by([1, 2, 3], key=lambda i: i == 2)
            {False: [1, 3], True: [2]}

            >>> group_by(range(10), key=lambda i: i % 3)
            {0: [0, 3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

            >>> Utils.group_by(json_data, key=lambda k: k['class'])
            {"mammal": [{"name": "leopard", "class": "mammal", "order": "Carnivora", "max_speed": "58.0"}], "bird": [{"name": "parrot", "class": "bird", "order": "Psittaciformes", "max_speed": "24.0"}]}
        """

        results: Dict[_K, List[_V]] = {}

        for item in items:
            # results.setdefault(value, set()).add(key)
            group_key = key(item)
            # print(f"group_key => {group_key}, item => {item}")
            results.setdefault(group_key, list()).append(item)

        return results


# Starting Point
print()
print("print args")
print(Utils.print_args('Hi', 'Rohtash', 2024, True))
print()

print()
print("print keyword args")
print(Utils.print_kwargs(firstName='Rohtash', lastName='Lakra', age=21))
print()

print()
print("Generating UUID:")
print(Utils.generate_uuid())
print()
print(list(Utils))

user_agent = '{platform: "iOS", osVersion: "1.0", deviceType: "mobile/tablet", deviceId: "1234-5678-9014", appVersion: "1.0.0"}'
print(f"user_agent:{user_agent}")
print("Parsed User-Agent:")
print(Utils.parse_user_agent(user_agent))
print()

print()
print("Execute HTTP Request")
url = 'https://www.python.org/'
# print(Utils.execute(url))
print()

json_data = [
    {
        "name": "leopard",
        "class": "mammal",
        "order": "Carnivora",
        "max_speed": "58.0"
    },
    {
        "name": "monkey",
        "class": "mammal",
        "order": "Primates",
        "max_speed": "NaN"
    },
    {
        "name": "lion",
        "class": "mammal",
        "order": "Carnivora",
        "max_speed": "80.2"
    },
    {
        "name": "parrot",
        "class": "bird",
        "order": "Psittaciformes",
        "max_speed": "24.0"
    },
    {
        "name": "falcon",
        "class": "bird",
        "order": "Falconiformes",
        "max_speed": "389.0"
    }
]

print()
print("Group by Class")
group_by_class = {}
for entry in json_data:
    group_by_class.setdefault(entry['class'], []).append(entry)

print(json.dumps(group_by_class))
print()

print()
print("Group by Class type")
group_by_class = {}
group_by_class = Utils.group_by(json_data, key=lambda k: k['class'])
print(json.dumps(group_by_class))
print()
