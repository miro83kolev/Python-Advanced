def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    basket = set()
    products = []
    for product, product_data in kwargs.items():
        if len(basket) == 5:
            break
        price = product_data[0]
        quantity = product_data[1]
        final_price = price * quantity

        if budget >= final_price:
            basket.add(product)
            products.append(f'You bought {product} for {final_price:.2f} leva.')
            budget -= final_price

    return '\n'.join(products)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
