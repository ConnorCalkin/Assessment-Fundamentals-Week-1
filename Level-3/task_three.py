"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_item_invoice(item_string: str) -> str:
    result = ""
    words = item_string.split(" ")
    result += " ".join(words[:-1])
    price = words[-1]
    price_float = float(price[1:])
    new_price = price_float * 0.8
    result += f" {new_price:.2f}"


def generate_invoice(receipt_string: str) -> str:
    '''
    Generates an invoice given a receipt
    '''
    result = ""
    lines = receipt_string.split('\n')
    items_strings = lines[:-1]
    total_string = lines[-1]

    for item_string in items_strings:
        result += generate_item_invoice(item_string)

    return  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
        Milk x 1 - £0.80
        Butter x 1 - £1.20
        Total: £5.60"""
    print(generate_invoice(receipt_string))
