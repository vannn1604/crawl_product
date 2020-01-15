import psycopg2
import json

hostname = "localhost"
username = "postgres"  # the username when you create the database
password = "admin"  # change to your password
database = "tizzie"

'''
def queryQuotes(conn):
    cur = conn.cursor()
    cur.execute("""select * from products""")
    rows = cur.fetchall()

    for row in rows:
        print(row)
'''

connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
cur = connection.cursor()
with open("product.json") as json_file:
    data_product = json.load(json_file)
    for data in data_product:
        cur.execute(
            "insert into products(name,brand,specs) values(%s,%s,%s)",
            (data["name"], data["brand"], json.dumps(data["specs"]),),
        )
        connection.commit()
        cur.execute(
            "select id from products where name=%s", (data["name"],),
        )
        product_id = cur.fetchone()
        print(product_id[0])
        for review in data["reviews"]:
            cur.execute(
                "insert into product_review(product,data) values(%s,%s)",
                (product_id[0], json.dumps(review)),
            )
            connection.commit()
connection.close()
