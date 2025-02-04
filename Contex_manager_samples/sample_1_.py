class Yolo:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('exception')
        else:
            print('exiting')
        return True


with Yolo() as y:
    print('normal code')
    raise Exception('oops')

print('Next code')
