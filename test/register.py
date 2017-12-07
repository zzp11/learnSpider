class a:
    @classmethod
    def register(cls, name, func):
        def f(cls):
            return func()
        setattr(cls, name, f)

hello = lambda : 'hello'

#a.register('hello', hello)

aa = a()

aa.register('hello', hello)
print aa.hello()