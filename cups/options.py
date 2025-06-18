from typing import (
    Dict,
    Optional,
)

from cups.types import cupsOption


def getOption(name: str, options: Dict[str, cupsOption]) -> Optional[cupsOption]:
    return options[name]
