def magic(**kwargs):
    # styles = [x for x in iterable]
    styles = ''.join(f'{key}: {value}; ' for key, value in kwargs.items())
    html = f'<p style="{styles}"></p>'
    print(html)


css_dict = {
    'color': 'peru',
    'text-decoration': 'underline',
    'font-size': '2rem'
}
# print(css_dict.items())
# print(css_dict.keys())
# print(css_dict.values())
magic(**css_dict)