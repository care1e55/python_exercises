
def myxml(tag, content='', **kwargs) -> str:
    kwargs_str = [ f'{key}={value}' for key, value in kwargs.items() ]
    return f'<{tag} {" ".join(kwargs_str)}>{content}</{tag}>'

if __name__ == '__main__':
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a=1, b=2, c=3))
