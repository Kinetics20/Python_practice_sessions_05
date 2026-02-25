from collections import defaultdict
import pandas as pd
from typing import TypedDict, Any, TypeGuard
from collections.abc import Iterable


class ScoreRecords(TypedDict):
    """
    Represents a single game score record.
    """
    date: str
    game: str
    player: str
    level: int
    score: int


def is_score_record(obj: Any) -> TypeGuard[ScoreRecords]:
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


data: list[ScoreRecords] = [
    {"date": "2026-02-20", "game": "SpaceWar", "player": "Alice", "level": 3, "score": 120},
    {"date": "2026-02-20", "game": "SpaceWar", "player": "Bob", "level": 2, "score": 150},
    {"date": "2026-02-20", "game": "ZombieRun", "player": "Alice", "level": 1, "score": 80},
    {"date": "2026-02-20", "game": "ZombieRun", "player": "Charlie", "level": 2, "score": 95},
    {"date": "2026-02-21", "game": "SpaceWar", "player": "Alice", "level": 4, "score": 200},
    {"date": "2026-02-21", "game": "SpaceWar", "player": "Bob", "level": 3, "score": 180},
    {"date": "2026-02-21", "game": "ZombieRun", "player": "Charlie", "level": 3, "score": 110},
]


def max_score(coll):
    res = {}

    for row in coll:
        key = (row['date'], row['game'])
        score = row['score']

        if key not in res:
            res[key] = score
        else:
            res[key] = max(res[key], score)

    return res


# print(max_score(data))

def max_score_2(coll):
    res = {}

    for row in coll:
        key = (row['date'], row['game'])
        score = row['score']

        res[key] = max(score, res.get(key, float('-inf')))

    return res


# print(max_score_2(data))


def max_score_3(coll):
    res = defaultdict(lambda: float('-inf'))

    for row in coll:
        key = (row['date'], row['game'])
        res[key] = max(res[key], row['score'])

    return res


# print(max_score_3(data))


def max_score_4(coll):
    df = pd.DataFrame(coll)
    return df.groupby(['date', 'game'])['score'].max()


# print(max_score_4(data))


Key = tuple[str, str]
Score = int


def highest_score_per_game(coll: Iterable[ScoreRecords]) -> dict[Key, Score]:
    result: dict[Key, Score] = {}

    for row in coll:
        if not is_score_record(row):
            raise ValueError("Invalid payload")

        key: Key = (row['date'], row['game'])
        score: Score = row['score']

        current_max = result.get(key)

        if current_max is None or score > current_max:
            result[key] = score

    return result


print(highest_score_per_game(data))
