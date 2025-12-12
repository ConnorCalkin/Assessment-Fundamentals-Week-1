"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_item_invoice(item_string: str) -> str:
    '''
    takes in a line from a receipt such as: Bread x 2 - £3.60
    then, it returns what it would be in the invoice: Bread x 2 - £2.88
    '''
    result = ""
    words = item_string.split(" ")
    result += " ".join(words[:-1])
    price = words[-1]
    price_float = float(price[1:])
    new_price = price_float * 0.8
    result += f" £{new_price:.2f}"
    return result


def generate_total_invoice(total_string: str):
    '''
    takes in a total line from a receipt: Total: £5.60
    and returns the invoice version:
    Total: £4.48
    VAT: £1.12
    Total inc VAT: £5.60
    '''
    price_string = total_string.split(" ")[1]
    total_inc_vat = float(price_string[1:])
    new_total = total_inc_vat * 0.8
    vat = total_inc_vat - new_total

    return f"Total: £{new_total:.2f}\nVAT: £{vat:.2f}\nTotal inc VAT: £{total_inc_vat:.2f}"


def generate_invoice(receipt_string: str) -> str:
    '''
    Generates an invoice given a receipt
    '''
    result = "VAT RECEIPT\n\n"

    lines = receipt_string.split('\n')
    items_strings = lines[:-1]
    total_string = lines[-1]

    for item_string in items_strings:
        result += generate_item_invoice(item_string)
        result += "\n"

    if len(items_strings) != 0:
        result += "\n"

    result += generate_total_invoice(total_string)

    return result


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
