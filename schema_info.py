import sqlite3

def get_schema_info(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    schema_info = {}
    
    # Get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        
        # Get the column information for each table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        schema_info[table_name] = []
        for column in columns:
            col_name = column[1]
            col_type = column[2]
            schema_info[table_name].append((col_name, col_type))
    
    conn.close()
    return schema_info
