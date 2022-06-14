def document_it(func):
    def show_info(*args, **kwargs):
        print('function name: ',func.__name__)
        print('args: ',args)
        print('kwargs: ',kwargs)
        result=func(*args, **kwargs)
        print('result: ',result)
    return show_info


class Cat:
    def __init__(self, name):
        self.name =name


@document_it
def sum(a,b):
    return a+b

cat=Cat('Kuro')
print(cat.name)
