from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)


class Contact:
    def __init__(self, contact_tuple):
        self.id = contact_tuple[0]
        self.name = contact_tuple[1]
        self.phone = contact_tuple[2]
        self.email = contact_tuple[3]
        self.address = contact_tuple[4]
        self.user = contact_tuple[5]


def query(sql):
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        rows = cur.execute(sql)
        return [Contact(row) for row in rows.fetchall()]


def get_contacts():
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM contacts")
        return [Contact(row) for row in rows.fetchall()]


@app.route('/')
def home():
    return render_template("home.html", contacts=get_contacts())


@app.route('/delete')
def delete():
    query(f"DELETE FROM contacts WHERE id={request.args['id']}")
    return home()
