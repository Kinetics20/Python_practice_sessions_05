def create_product(name, price):
    return {'name': name, 'price': price}


def with_calc_price(product):
    product['price'] = product['price'] * 1.23
    return product


def with_calc_discount(product):
    product['price'] = product['price'] * 0.9
    return product


def add_producer(product, producer):
    product['producer'] = producer
    return product


product_1 = create_product('laptop', 1000)
product_2 = create_product('laptop', 500)

print(product_1, with_calc_discount(with_calc_price(product_2)))


# fn_mapping = {
#     'calc_price': with_calc_price,
#     'calc_discount': with_calc_discount
# }
#
# user_choices = ['calc_price', 'calc_discount']
#
# reduce(lambda acc, ce: fn_mapping[ce](acc), user_choices, product_2)
