import psycopg2

conn = psycopg2.connect(
    dbname="db",
    user="username",
    password="password",
    host="host",
    port="port"
)

cur = conn.cursor()

# Execute query
cur.execute("SELECT * FROM table")

# Fetch results
results = cur.fetchall()

for row in results:
    print(row)
