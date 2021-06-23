"""
directory_printer.py

Lorem Ipsum Whatever.

contains functions to return a filtered list
of contents from dir(parameter).
"""


from re import match


def public_module_or_class_contents(module_or_class=__builtins__):
    """    if not x.startswith('_') and not re.match(b'^[A-Z]{1,}[A-Z_]{1,}', bytes(x, 'utf8'))    """
    
    vals = [
            x for x in dir(module_or_class) \
            if not x.startswith('_') \
                and not match(b'^[A-Z]{1,}[A-Z_]{1,}', bytes(x, 'utf8'))
    ]
    
    return vals


def module_or_class_constants(module_or_class=__builtins__):
    """    if not re.match(b'^[^A-Z]+[_A-Z0-9]*$', bytes(x, 'utf8'))    """

    vals = [
        x for x in dir(module_or_class) \
        if not match(b'^[^A-Z]+[_A-Z0-9]*$', bytes(x, 'utf8'))
    ]

    return vals


"""     Doesn't work:
def recursive_dir_public_contents(module_or_class=__builtins__):
    \"\"\" is a broken generator \"\"\"

    vals = public_module_or_class_contents(module_or_class)
    
    for x in public_module_or_class_contents(module_or_class):
        vals = x
        try:
            recursive_dir_public_contents(x)
        except Exception as e:
            print(e)
            pass
        finally:
            yield vals
"""