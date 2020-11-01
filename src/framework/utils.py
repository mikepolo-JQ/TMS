from framework.consts import DIR_ASSETS
from framework.consts import DIR_STATIC


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def read_assets(file_name: str) -> bytes:
    path = DIR_ASSETS / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload
