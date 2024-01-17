from faker import Faker
import sqlite3


def add_contacts():
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        for i in range(20):
            profile = Faker(locale="he_IL").simple_profile()
            phone = Faker(locale="he_IL").phone_number()
            cur.execute(
                f"INSERT INTO contacts (name, phone, email, address) VALUES ('{profile["name"]}','{phone}','{profile["mail"]}','{profile["address"]}')")
