
def ensure_trailing_slash(value):
    if not isinstance(value, str):
        raise TypeError("ensure_trailing_slash filter expects a string")
    return value if value.endswith('/') else value + '/'

class FilterModule(object):
    def filters(self):
        return {
            'ensure_trailing_slash': ensure_trailing_slash
        }
