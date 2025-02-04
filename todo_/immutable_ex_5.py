from dataclasses import dataclass
import dataclasses



@dataclass(frozen=True)
class Todo:
    name: str
    status: str = 'pending'



@dataclass(frozen=True)
class TodoList:
    todos: tuple[Todo, ...]


t1 = Todo('Python', 'Failure')
t2 = Todo('Data Science')
t3 = Todo('MLOPS')

t_coll = TodoList((t1, t2, t3))

# print(t_coll)

def change_todo_name(todo: Todo, name: str) -> Todo:
    # return Todo(**(asdict(todo)) | {'name': name})
    return dataclasses.replace(todo, name=name)


def update_todos(todo_list: TodoList, prev_todo: Todo, next_todo: Todo) -> TodoList:
    # def replace_todo(todo: Todo) -> Todo:
    #     if todo is not prev_todo:
    #         return todo
    #     return next_todo

    # return TodoList(tuple(map(replace_todo, todo_list.todos)))
    # return TodoList(tuple(map(lambda todo: todo if todo is not prev_todo else next_todo)))


    result = []

    for todo in todo_list.todos:
        if todo is not prev_todo:
            result.append(todo)
        else:
            result.append(next_todo)


    t_result = tuple(result)
    return TodoList(t_result)


# def change_todos(todo_list: TodoList, prev_todo: Todo, new_todo: Todo) -> TodoList:
#     return TodoList(tuple(todo if todo != prev_todo else new_todo for todo in todo_list.todos))

print(t_coll)
tx = change_todo_name(t2, 'Hommpjpjije')
t_call = update_todos(t_coll, t2, tx)
print(t_coll)
# print(tx)
