def calc_discount(price: float, discount: float) -> float:
    """
    Calculates the price after applying a discount.

    :param price: The original price of the product (must be greater than 0).
    :type price: float
    :param discount: The discount percentage (must be greater than 0 and less than 100).
    :type discount: float
    :return: The price after applying the discount.
    :rtype: float
    :raises ValueError: If price is not greater than 0 or if discount is not strictly between 0 and 100.
    """
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    if not (0 < discount < 100):
        raise ValueError("Discount must be between 0 and 100")

    return price * (1 - discount / 100)
