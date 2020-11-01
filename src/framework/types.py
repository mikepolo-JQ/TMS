import dataclasses
from typing import NamedTuple

# ResponseT = Tuple[str, dict, bytes]


class ResponseT(NamedTuple):
    status: str
    headers: dict
    payload: bytes


@dataclasses.dataclass
class RequestT:
    method: str
    path: str
    headers: dict


class HandlerRequest:
    def __init__(self, handler, file_name):
        self.handler = handler
        self.file_name = file_name
