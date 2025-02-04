
def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner


def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner


def inner_wrapper(fn, tag, tag_2, **styles):
    css_styles = {
        property_name: ''.join(f'{key}: {value}; ' for key, value in property_val.items())
        for property_name, property_val in styles.items()
    }

    # username_styles = ''.join(f'{key}: {value}; ' for key, value in styles['username'].items())
    # title_styles = ''.join(f'{key}: {value}; ' for key, value in styles['title'].items())

    def inner(name):
        result = fn(f'<{tag_2} style="{css_styles.get('username', '')}">{name}<{tag_2}/>')
        return f'<{tag} style="{css_styles.get('title', '')}">{result}</{tag}>'
    return inner


def gen_html(cb=None, *, tag='h1',tag_2='b', **styles):
    if callable(cb):
        return inner_wrapper(cb, tag, tag_2, **styles)


    def wrapper(cb_):
        return inner_wrapper(cb_, tag, tag_2, **styles)

    return wrapper


def gen_html_template(template_path, output_path):
    def wrapper(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            with open(template_path) as template:
                template_text = template.read().replace('{{ placeholder }}', result)

            with open(output_path, mode='w') as file:
                file.write(template_text)

        return inner

    return wrapper


# def gen_html(fn):
#     def inner(name):
#         result = fn(f'<b>{name}<b/>')
#         return f'<h1>{result}</h1>'
#
#     return inner


# @capitalize
# @gen_html(tag='h3',tag_2='b')
# def hello(name):
#     return f'<h1>Hello <b>{name}<b/></h1>'



css_dict = {
    'username': {
        "color": "transparent",
        "text-shadow": "0 0 10px rgba(255,69,0,0.8), 0 0 20px rgba(255,140,0,0.8), 0 0 30px rgba(255,69,0,0.6), 0 0 40px rgba(255,0,0,0.8)",
        "background": "linear-gradient(to right, #ff4500, #ff8c00, #ff4500)",
        "background-clip": "text",
        "-webkit-background-clip": "text",
        "-webkit-text-fill-color": "transparent",
        "font-size": "2rem",
        "animation": "flicker 2s infinite alternate",
        "font-family": "'Arial', sans-serif"
    },
    'title': {}
}

css_dict_bye = {
 'title':{   "color": "transparent",
    "background": "linear-gradient(to right, #00bfff, #1e90ff, #4682b4, #00bfff)",
    "background-clip": "text",
    "-webkit-background-clip": "text",
    "-webkit-text-fill-color": "transparent",
    "font-size": "2rem",
    "animation": "wave 4s infinite linear, shimmer 2s infinite alternate",
    "text-shadow": "0 2px 5px rgba(0, 191, 255, 0.5), 0 -2px 10px rgba(30, 144, 255, 0.7)",
    "font-family": "'Arial', sans-serif"}
}




@gen_html_template('template.html', 'hello.html')
@capitalize
@gen_html(**css_dict)
def hello(name):
    return f"Hello {name}"

@gen_html_template('template.html', 'bye.html')
@capitalize
@gen_html(tag='h2',tag_2='C', **css_dict_bye)
def bye(name):
    return f"Bye {name}"


# def bye(name):
#     return f'<h1>Bye <b>{name}<b/></h1>'

print(hello("ola")) # <h1>Hello <b>Ola<b/></h1>
print(bye("lech"))  # <h1>Bye <b>Lech<b/></h1>
