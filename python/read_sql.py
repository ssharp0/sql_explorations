import pandas as pd
import sqlite3

conn = sqlite3.connect(':memory:')
df = pd.read_sql_query('SELECT * FROM table', conn)
