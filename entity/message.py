#
# Author: Rohtash Lakra
#
from dataclasses import dataclass


@dataclass
class Message:
    event: str

    def __repr__(self):
        return f"Message <event={self.event}>"
