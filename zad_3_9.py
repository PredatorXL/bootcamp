from datetime import datetime


def log(funkcja):
    def dekorator(*args, **kwargs):
        print(str(datetime.now()))
        print(funkcja.__name__)
        print(','.join(args))
        return funkcja(*args, **kwargs)
    return dekorator

@log
def foo(arg):
    print(f'To jest {arg}')


foo('aaaaaaaaa')