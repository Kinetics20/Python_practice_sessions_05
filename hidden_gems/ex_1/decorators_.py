
def upper(fn):
    def inner(*args):
        args = [arg.title() for arg in args]
        # kwargs = {k: v.title() for k, v in kwargs}
        return fn(*args)

    return inner


def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner

def html(tag='h1'):
    def wrapper(fn):
        def inner(*args):
            args_ = list(args)
            args_[0] = '<b>' + args[0]
            args_[-1] = args_[-1] + '</b>'

            html_text = f'<{tag}>{fn(*args_)}</{tag}>'
            return html_text

        return inner
    return wrapper

@upper
@html()
def bye(name, last_name, /):
    return f'Bye, {name} {last_name}!'


@upper
@html(tag='h2')
def hello(name, /):
    return f'Hello, {name}!'

print(bye('John', 'Smith'))
print(hello('John'))
