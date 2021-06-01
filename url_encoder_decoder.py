"""
test
test backslashes
test decoding & encoding
build gui
test indexes in decoding function
"""


unreserved_characters = [
    'A','B','C','D','E','F','G','H',
    'I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X',
    'Y','Z',
    'a','b','c','d','e','f','g','h',
    'i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x',
    'y','z',
    '0','1','2','3','4','5','6','7','8','9',
    '-','_','.']

special_characters = {
        '!': '%21',
        '*': '%2A',
        "'": '%27',
        '(': '%28',
        ')': '%29',
        ';': '%3B',
        ':': '%3A',
        '@': '%40',
        '&': '%26',
        '=': '%3D',
        '+': '%2B',
        '$': '%24',
        ',': '%2C',
        '/': '%2F',
        '?': '%3F',
        '#': '%23',
        '[': '%5B',
        ']': '%5D',
        '%': '%25',
        ' ': '%20',
        '"': '%22',
        '%': '%25',
        '-': '%2D',
        '.': '%2E',
        '<': '%3C',
        '>': '%3E',
        '\\': '%5C',
        '^': '%5E',
        '_': '%5F',
        '`': '%60',
        '{': '%7B',
        '|': '%7C',
        '}': '%7D',
        '~': '%7E'
    }

encoded_characters = {v: k for k, v in special_characters.items()}

def url_encode(string):
    #
    new_string = ''
    for character in string:
        if character in unreserved_characters:
            new_string += character
        else:
            try:
                new_string += special_characters[character]
            except KeyError:
                print('KeyError:\t'+character+' not found')
                new_string += character
    #
    return new_string

def url_decode(string):
    #
    new_string = ''
    index = 0
    skip = 0
    for character in string:
        if skip > 0:
            skip -= 1
            continue
        if character == '%':
            try:
                new_string += encoded_characters[string[index:index+3]]
            except KeyError:
                print('KeyError:\t'+string[index:index+3])
                new_string += string[index:index+3]
            finally:
                skip = 2
                index += 3
        else:
            new_string += character
            index += 1
    #
    return new_string


if __name__ == '__main__':

    import tkinter as tk

    root = tk.Tk()
    root.title('URL Encoder / Decoder')

    ipt = tk.StringVar()
    #opt = tk.StringVar()

    tk.Label(root, text='Input:').grid(row=1, column=1)
    _input = tk.Entry(root, width=72, bg='white', textvariable=ipt)
    _input.grid(row=1, column=3)


    tk.Label(root, text='Output:').grid(row=3, column=1)
    _output = tk.Entry(root, width=72, bg='white')
    _output.grid(row=3, column=3)

    tk.Button(root, text='Encode!', command=lambda x=_output: [x.delete(0, len(x.get())), x.insert(0, url_encode(ipt.get()))]).grid(row=2, column=1)
    tk.Button(root, text='Decode!', command=lambda x=_output: [x.delete(0, len(x.get())), x.insert(0, url_decode(ipt.get()))]).grid(row=2, column=2)

    root.mainloop()

