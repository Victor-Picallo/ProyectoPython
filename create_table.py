from connect import get_connection

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS profesores(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    )
    """
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    
    conn.commit()
    conn.close()
    
    if __name__ == "__main__":
        create_table()