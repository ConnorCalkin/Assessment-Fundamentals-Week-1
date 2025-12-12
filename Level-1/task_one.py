
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    '''
    adds the given item and returns an updated dictionary
    '''
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    '''
    creates a reciept showing all of the prices of the items in the basket
    '''
    if len(basket) == 0:
        return "Basket is empty"
    receipt = ""
    total = 0
    for item in basket:
        price = item["price"]
        price_str = f"£{item["price"]:.2f}"
        if price == 0:
            price_str = "Free"

        receipt += (f"{item["name"]} - {price_str}\n")
        total += item["price"]
    total = round(total, 2)
    receipt += f"Total: £{total:.2f}"
    return receipt


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
