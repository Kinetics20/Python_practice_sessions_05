class Singleton:

    check = None

    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()

        return Singleton._instance


s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2

s1.check = 42
assert s1.check == s2.check