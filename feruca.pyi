from typing import Literal

def collate(
    strings: list[str],
    tailoring: Literal["default", "ArabicScript", "ArabicInterleaved"] = "default",
) -> list[str]: ...
