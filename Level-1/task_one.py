
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    '''
    creates a reciept showing all of the prices of the items in the basket
    '''
    receipt = ""
    total = 0
    for item in basket:
        receipt += (f"{item["name"]} - £{item["price"]:.2f}\n")
        total += item["price"]
    receipt += f"Total: £{total}"
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
