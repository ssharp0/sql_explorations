import pandas as pd

def df_to_sql(df, output_file, sql_dialect='mysql'):
    # Convert DataFrame to SQL
    if sql_dialect == 'mysql':
        sql = df.to_sql_string(index=False)
    elif sql_dialect == 'postgresql':
        sql = df.to_sql_string(index=False, index_label='id')
    else:
        raise ValueError("Unsupported SQL dialect")

    # Write SQL to file
    with open(output_file, 'w') as f:
        f.write(sql)

# usage
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df_to_sql(df, 'output.sql', sql_dialect='mysql')
