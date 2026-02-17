from dataclasses import dataclass
from datetime import date


@dataclass
class Classroom:
    id: int
    name: str
    created: date
    active: bool = True
