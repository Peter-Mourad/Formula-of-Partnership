from . import sheet

def get_users():
    conn = sheet.get_gsheets_connection("Partners Registration Form")
    return sheet.read_gsheet(conn)


def add_user(user):
    conn = sheet.get_gsheets_connection("Partners Registration Form")
    row = []
    for d in user:
        row.append(user[d])
    sheet.write_gsheet(conn, row)


def get_user_by_code(partner_code):
    rows = get_users()
    for row in rows:
        if row["partner_code"] == partner_code and row["is_approved"]:
            return row
    return None
