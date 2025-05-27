import os
from mcp.server.fastmcp import FastMCP
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql
from tabulate import tabulate
from datetime import date

load_dotenv()

mcp = FastMCP("My PostGres SQL DB")

# We’ll open the connection only when needed — not globally
def get_connection():
    return psycopg2.connect(
        dbname="smartscheduler",
        host="smartscheduler-db.cxa8eks2ozot.ap-south-1.rds.amazonaws.com",
        port=5432,
        user="admin_db",
        password=os.getenv("RDS_POSTGRES_KEY"),
    )

@mcp.tool()
async def query_db(sql_query: str):
    """
    Execute a SQL query inside the study_sessions table.
    Handles SELECT, INSERT, UPDATE, and DELETE operations.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql_query)

        # Check if the command is SELECT or others
        if cursor.description:  # SELECT returns description
            get_records = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            return tabulate(get_records, headers=column_names, tablefmt="psql")
        else:
            conn.commit()
            return f"Query executed successfully: {sql_query.split()[0].upper()}"

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
if __name__ == "__main__":
    mcp.run()