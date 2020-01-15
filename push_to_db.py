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
            "insert into products(name,brand,reviews,specs) values(%s,%s,array[%s]::json[],%s)",
            (data["name"], data["brand"], json.dumps(data["reviews"]), json.dumps(data["specs"]),),
        )
        connection.commit()
# cur.execute("""select * from products""")
# rows = cur.fetchall()

# for row in rows:
#     print(row)
# cur.close()
connection.close()
