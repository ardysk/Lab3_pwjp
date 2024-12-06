class ToUpper(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        text = self.func(*args, **kwargs)
        return text.upper()

@ToUpper
def return_name():
    return 'Adam'

print(return_name())