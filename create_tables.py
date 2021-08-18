import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    try:
        print("Trying To Create Databases and Checking Connections")
        # connect to default database
        conn = psycopg2.connect(user="student",password="student",host="127.0.0.1",port="5433",database="studentdb")

        conn.set_session(autocommit=True)
        cur = conn.cursor()

        # create sparkify database with UTF8 encoding
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

        # close connection to default database
        conn.close()    
        
        # connect to sparkify database
        conn = psycopg2.connect(user="student",password="student",host="127.0.0.1",port="5433",database="sparkifydb")
        cur = conn.cursor() 

        print("Database Creation and Operations Successfuly Completed.")

    except (Exception, psycopg2.Error) as error:
            if(conn):
                print("Connection or Operation Fail. Please Check Your Connection String and Parameters", error)
    finally:
        if(conn):
            return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    # drop_tables(cur, conn)
    # create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()