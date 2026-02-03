import functools

def log_around(cb):
    @functools.wraps(cb)
    def wrapper(*args):
        print('Params', args)
        result = cb(*args)
        print('Return', result)
        return result
    return wrapper

@log_around
def task_one(*args):
    return str(args)

print(task_one())
print(task_one(1, 2, 3, 45))
print(task_one.__name__)

# task_one_log_around = log_around(task_one)
# task_one_log_around(1, 2, 3, 4, 5)
