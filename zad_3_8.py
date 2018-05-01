def bold(funkcja):
    def dekorator(*arg, **kwargs):
        return '<b>' + str(funkcja(*arg, **kwargs)) + '<b>'
    return dekorator

def italics(funkcja):
    def dekorator(*arg, **kwargs):
        return '<i>' + str(funkcja(*arg, **kwargs)) + '<i>'
    return dekorator

def underline(funkcja):
    def dekorator(*arg, **kwargs):
        return '<u>' + str(funkcja(*arg, **kwargs)) + '<u>'
    return dekorator



@bold
@italics
@underline
def hello(name):
    return f"To jest {name}"

print(hello('Python'))