from collections import defaultdict
import pandas as pd

data = [
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

print(max_score_4(data))
