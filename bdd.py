from mysql import connector
from dotenv import load_dotenv
from os import getenv


load_dotenv()

print(getenv("DB"))

db = connector.connect(
    host="localhost",
    database=getenv('DB_NAME'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASS')
)
cursor = db.cursor(dictionary=True)

# username = "faust"
# first_name = "Sebastien"
# last_name = "Minguy"
# # cursor.execute("INSERT INTO user (username, first_name, last_name) VALUES ('Oawx', 'Sandra', 'LE Roi')")
# # cursor.execute("INSERT INTO user (username, first_name, last_name) VALUES (%s, %s, %s), (username, first_name, last_name)")
# cursor.execute(
#     "INSERT INTO user (username, first_name, last_name) "
#     "VALUES (%(user_username)s, %(user_first_name)s, %(user_last_name)s) ",
#     {"user_username": username, "user_first_name": first_name, "user_last_name": last_name})
# db.commit()

query = "SELECT username FROM user WHERE id = %(id)s"
cursor.execute(query, {"id": 4})
# print(cursor.fetchall())
# print(cursor.fetchone())
user = cursor.fetchone()
print(user["username"])

# while True:
#     user = cursor.fetchone()
#     if user is None:
#         break
#     else:
#         print(user['username'])
