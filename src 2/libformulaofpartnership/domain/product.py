import gspread
from . import sheet


def store_product(dict_data):
    conn = sheet.get_gsheets_connection("Products Sheet")
    row = []
    for d in dict_data:
        v = str(dict_data[d])
        # Protect From G sheet formula injection
        v = v.lstrip('=')
    
        row.append(v)
    sheet.write_gsheet(conn, row)


def store_products(data, partner_code):
    products = []
    for product in data:
        # get the variants and check if they are a list
        variants = eval(product['variants'])
        if isinstance(variants, list):
            for v in variants:
                products.append(
                    {
                        "name": product["name"],
                        "image": product["image"],
                        "price": product["price"],
                        "partner_code": partner_code,
                        "variant": v,
                    }
                )
        else:
            products.append(
                {
                    "name": product["name"],
                    "image": product["image"],
                    "price": product["price"],
                    "partner_code": partner_code,
                    "variant": variants,
                }
            )

    for product in products:
        store_product(product)
    return product


def get_partner_products(partner_code):
    conn = sheet.get_gsheets_connection("Products Sheet")

    rows = sheet.read_gsheet(conn)

    products = []
    for row in rows:
        if row.get("partner_code") == partner_code:
            products.append(row)

    return products
