from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


from uuid import UUID, uuid4
from datetime import datetime



class RevievResult(StrEnum):
    """Support study outcomes for a review event."""

    AGAIN = "again"
    HARD = "hard"
    GOOD = "good"


@dataclass(frozen=True, slots=True)
class Flashcards:
    """Immutable flashcard entity."""

    card_id: UUID
    front: str
    back: str
    created_at: datetime
    updated_at: datetime
    review_count: int = 0
    interval_days: int = 0
    last_result: RevievResult | None = None


z = Flashcards(
    card_id=UUID(f'{uuid4()}'),
    front='front',
    back='back',
    created_at=datetime.now(),
    updated_at=datetime.now(),
    last_result=RevievResult.HARD
)

m = RevievResult.HARD

# print(z.card_id, z.front, z.back)
print(z)
print(z.last_result)
# print(m)
print(RevievResult.__members__)
print(RevievResult(value='hard'))
# print(tuple(RevievResult.__members__))
# print(set(RevievResult.__members__))
# print(RevievResult.HARD.value)
# print(RevievResult.HARD.name)