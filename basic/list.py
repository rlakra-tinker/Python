# mutable collection
scientist_json = [
    {
        "name": "Rohtash",
        "field": "Computer Science",
        "born_year": 1975,
        "win_prize": "false"
    },
    {
        "name": "Lakra",
        "field": "English",
        "born_year": 1978,
        "win_prize": "false"
    }
]

# mutable collection objects
print()
print(scientist_json)

print()
print(scientist_json[1]["name"])
print()

print()
scientist_json[1]["name"] = 'Rohtash Singh'
print(scientist_json[1]["name"])
print()


# immutable collections
import collections
Scientist = collections.namedtuple("Scientist", [
    "name", 
    "field",
    "born_year",
    "win_prize"
    ])


from pprint import pprint
print("----------------->")

# add scientists in the immutable list
scientists = []
for scientist in scientist_json:
    print(scientist)
    scientists.append(Scientist(scientist["name"], scientist["field"], scientist["born_year"], scientist["win_prize"]))

scientists_tuple = (scientists)

print("<--------- scientists -------->")
pprint(scientists)

# read first scientist
rohtash = scientists[1]
print("<--------- rohtash -------->")
print(rohtash)
print()

print("<--------- read named-tuple key -------->")
print()
# rohtash.name = "Rohtash Lakra"
print(rohtash.name)
# print(rohtash)
print()

print("<--------- scientists_response -------->")
scientists_response = []
for scientist in scientist_json:
    scientists_response.append(Scientist(scientist["name"], scientist["field"], scientist["born_year"], scientist["win_prize"]))


print(scientists_response)
print()
for response in scientists_response:
    # print(response)
    print(f"scientist <{response.name}, {response.field}, {response.born_year}, {response.win_prize}>")

print()

print("<--------- scientists_result -------->")
scientists_result = [Scientist._make({
        'name': scientist["name"],
        'field': scientist["field"],
        'born_year': scientist["born_year"],
        'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
    }) for scientist in scientist_json]

print(scientists_result)
print()


print("<--------- results_by_expend -------->")
results_by_expend = []
results_by_expend.extend([{
        'name': scientist["name"],
        'field': scientist["field"],
        'born_year': scientist["born_year"],
        'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
    }for scientist in scientist_json])
results_by_expend.extend([{
        'name': scientist["name"],
        'field': scientist["field"],
        'born_year': scientist["born_year"],
        'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
    }for scientist in scientist_json])
print(results_by_expend)
print()

print("---------> scientists_tuple <--------")
print(scientists_tuple)
del scientists_tuple[0]
print()
print(scientists_tuple[0].name)


