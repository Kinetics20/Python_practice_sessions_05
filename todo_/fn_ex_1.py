def create_product(name, price, fn=None):
    product = {'name': name, 'price': price}
    if callable(fn):
        product['price'] = fn(price)
    return product


def calc_price(price):
    return price * 1.23


def calc_discount(price):
    return price * 0.9


product_1 = create_product('laptop', 1000, calc_price)
product_2 = create_product('laptop', 500, calc_discount)

print(product_1, product_2)
