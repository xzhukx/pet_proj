import psycopg

conn = psycopg.connect(dbname="users_1", user="postgres", host="localhost", password="191092191092p")

cur = conn.connect()

# sql_create_script = """
#
# CREATE TABLE Users
# (
#     id serial PRIMARY KEY
#     username VARCHAR(50)
#     password VARCHAR(50)
# );
# """
#
# cur.execute(sql_script)
# conn.commit()