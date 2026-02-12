class Sth:
    def upper(self, fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).upper()
        return wrapper

    def capital(self, fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).capitalize()
        return wrapper


a = Sth()

@a.capital
@a.upper
def sentence(txt):
    return txt

print(sentence('I have to go'))