def calculateDiscount(total, discount):
    discount_price = total * (discount/100)
    grand_total = total - discount_price
    return discount_price, grand_total


def currencyConverter(amount, rate):
    return amount * rate
