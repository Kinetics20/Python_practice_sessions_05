import functools

def log_around(cb):
    @functools.wraps(cb)
    def wrapper(*args):
        print('Params', args)
        print('Return', cb(*args))
        return cb(*args)

    return wrapper

@log_around
def task_one(*args):
    return str(args)

task_one()
task_one(1, 2, 3, 45)
print(task_one.__name__)

