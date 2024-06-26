import uuid
from enum import Enum

class Utils(Enum):

    @classmethod
    def generate_uuid(cls):
        return uuid.uuid4().hex

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

