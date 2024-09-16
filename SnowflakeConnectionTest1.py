import os
import snowflake.connector
from snowflake.snowpark import Session
from snowflake.core import Root

############################################################
# Establish a connection to Snowflake using environment variables
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

# Create a cursor object
cur = conn.cursor()

# Optionally, you can execute a simple query to test the connection
cur.execute("SELECT CURRENT_VERSION()")
version = cur.fetchone()
print("Snowflake version:", version[0])

# Close the cursor and connection when done
cur.close()
conn.close()
