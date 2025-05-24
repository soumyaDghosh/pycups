from typing import NamedTuple, List

class cupsOption(NamedTuple):
    name: str
    value: str

class cupsDest(NamedTuple):
    name: str
    instance: str | None
    is_default: bool
    options: List[cupsOption]