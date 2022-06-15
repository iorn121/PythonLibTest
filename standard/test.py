def document_it(func):
    def show_info(*args, **kwargs):
        print('function name: ', func.__name__)
        print('args: ', args)
        print('kwargs: ', kwargs)
        result = func(*args, **kwargs)
        print('result: ', result)
    return show_info


class Cat:
    def __init__(self, input_name):
        self.name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.name = input_name


@document_it
def sum(a, b):
    return a+b


cat = Cat('Kuro')
# cat.name

# cat.name = 'Shiro'

# cat.name
