import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321",
]

product_re = re.compile(r"PRD-[0-9]{5}")
products_valid=[]
for product in products:
    if product_re.fullmatch(product):
        products_valid.append(product)
print(products_valid)