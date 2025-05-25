import os
import psycopg2
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    dbname="smartscheduler",
    host="smartscheduler-db.cxa8eks2ozot.ap-south-1.rds.amazonaws.com",
    port=5432,
    user="admin_db",
    password=os.getenv("RDS_POSTGRES_KEY"),
)

cursor = conn.cursor()

st.title("Feedback Form")
st.markdown("**List down the items you have completed today!**")

# Fetch today's tasks
cursor.execute("""
    SELECT schedule, id  -- get primary key or unique id to update later
    FROM study_sessions
    WHERE DATE(created_at) = CURRENT_DATE;
""")
tasks = cursor.fetchall()

if not tasks:
    st.write("No scheduled tasks found for today.")
else:
    task_string = tasks[0][0]
    session_id = tasks[0][1]  # Assuming `id` column exists
    tasks_list = task_string.split('\n')
    tasks_list.append("Nothing!")

    completed_tasks = st.multiselect("Select completed tasks:", tasks_list)

    if st.button("Submit Form!"):
        # Serialize completed_tasks list to string (comma-separated)
        completed_str = ", ".join(completed_tasks) if completed_tasks else "Nothing"

        # Update the completed column for today’s study session
        cursor.execute("""
            UPDATE study_sessions
            SET completed = %s
            WHERE id = %s
        """, (completed_str, session_id))

        conn.commit()
        st.success("Your feedback has been recorded!")

cursor.close()
conn.close()
