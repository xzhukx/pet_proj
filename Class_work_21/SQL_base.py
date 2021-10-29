import psycopg2

conn = psycopg2.connect(dbname="Posts_1", user="postgres", password="191092191092p", host="localhost", port ="5432")
conn_1 = psycopg2.connect(dbname="users_1", user="postgres", password="191092191092p", host="localhost", port ="5432")
conn_2 = psycopg2.connect(dbname="Many_to_many_1", user="postgres", password="191092191092p", host="localhost", port ="5432")

cur = conn.cursor()
cur_1 = conn_1.cursor()
cur_2 = conn_2.cursor()

sql_create_script = """
CREATE TABLE user_mk (
    user_id   serial PRIMARY KEY,
    username text NOT NULL,
    price   numeric NOT NULL DEFAULT 0
    );
"""
cur.execute(sql_create_script)
conn.commit()