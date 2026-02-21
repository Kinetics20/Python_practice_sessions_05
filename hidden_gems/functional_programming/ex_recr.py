from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING, Any, TypeGuard

if TYPE_CHECKING:
    from collections.abc import Iterable


class ScoreRecord(TypedDict):
    """
    Represents a single game score record.
    """
    date: str
    game: str
    player: str
    level: int
    score: int


def is_score_record(obj: Any) -> TypeGuard[ScoreRecord]:
    if not isinstance(obj, dict):
        return False

    schema: dict[str, type] = {
        'date': str,
        'game': str,
        'player': str,
        'level': int,
        'score': int,
    }

    return all(
        key in obj and isinstance(obj[key], expected_type)
        for key, expected_type in schema.items()
    )



data: list[ScoreRecord] = [
    {"date": "2026-02-20", "game": "SpaceWar", "player": "Alice", "level": 3, "score": 120},
    {"date": "2026-02-20", "game": "SpaceWar", "player": "Bob", "level": 2, "score": 150},
    {"date": "2026-02-20", "game": "ZombieRun", "player": "Alice", "level": 1, "score": 80},
    {"date": "2026-02-20", "game": "ZombieRun", "player": "Charlie", "level": 2, "score": 95},
    {"date": "2026-02-21", "game": "SpaceWar", "player": "Alice", "level": 4, "score": 200},
    {"date": "2026-02-21", "game": "SpaceWar", "player": "Bob", "level": 3, "score": 180},
    {"date": "2026-02-21", "game": "ZombieRun", "player": "Charlie", "level": 3, "score": 110},
]

result = {}

for row in data:
    key = (row['date'], row['game'])
    score = row['score']

    # if key not in result:
    #     result[key] = score
    #
    # else:
    #     result[key] = max(result[key], score)

    result[key] = max(score, result.get(key, float('-inf')))

# print(result)


from collections import defaultdict


#
# result = defaultdict(lambda: float('-inf'))
# # result = defaultdict(int)
#
# for row in data:
#     key = (row['date'], row['game'])
#     result[key] = max(result[key], row['score'])
#
# print(result)


class ScoreRecord(TypedDict):
    """
    Represents a single game score record.
    """
    date: str
    game: str
    player: str
    level: int
    score: int


Key = tuple[str, str]
Score = int


def highest_score_per_game_per_day(records: Iterable[ScoreRecord]) -> dict[Key, Score]:
    result: dict[Key, Score] = {}

    for row in records:
        if not is_score_record(row):
            raise ValueError("Invalid payload")

        key: Key = (row["date"], row["game"])
        score: Score = row["score"]

        current_max = result.get(key)

        if current_max is None or score > current_max:
            result[key] = score

    return result


print(highest_score_per_game_per_day(data))
