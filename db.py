import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql, OperationalError, Error


load_dotenv()


def insert_values(topic, schedule):
    conn = psycopg2.connect(
        dbname="smartscheduler",
        host="smartscheduler-db.cxa8eks2ozot.ap-south-1.rds.amazonaws.com",
        port=5432,
        user="admin_db",
        password=os.getenv("RDS_POSTGRES_KEY"),
    )

    conn.autocommit = True
    print("Connection Successful")

    cursor = conn.cursor()
    try:
    
        insert_query = """
            INSERT INTO study_sessions (topic, schedule)
            VALUES (%s, %s)
            RETURNING id;
        """
        cursor.execute(insert_query, (topic, schedule))
        inserted_id = cursor.fetchone()[0]
        print(f"[INFO] Inserted new study session with id: {inserted_id}")
        return inserted_id
    except (Exception, Error) as error:
        print(f"[ERROR] Failed to insert data: {error}")
        return None
