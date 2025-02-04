from dataclasses import dataclass


@dataclass(frozen=True)
class Todo:
    name: str


@dataclass(frozen=True)
class TodoList:
    todos: tuple[Todo, ...]


t1 = Todo('Python')
t2 = Todo('Data Science')
t3 = Todo('MLOPS')

t_coll = TodoList((t1, t2, t3))

print(t_coll)