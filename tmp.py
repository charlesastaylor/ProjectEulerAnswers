def test(*args, **kwargs):
    print(args)
    print(type(args))
    print(isinstance(args, list))
    print(kwargs)
    print(type(kwargs))

test([1,2,3], x=5)