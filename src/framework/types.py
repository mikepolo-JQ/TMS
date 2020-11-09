import dataclasses
from typing import NamedTuple
from typing import Optional, Callable


class ResponseT(NamedTuple):
    status: str
    headers: dict
    payload: bytes


@dataclasses.dataclass
class RequestT:
    method: str
    path: str
    headers: dict
    kwargs: Optional[dict] = None
    query: Optional[str] = None
    body: Optional[dict] = None
    form_data: Optional[str] = None


HandlerT = Callable[[RequestT], ResponseT]


class StaticT(NamedTuple):
    content: bytes
    content_type: str

