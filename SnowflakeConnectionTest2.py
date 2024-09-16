 Define connection parameters from environment variables
connection_parameters = {
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA'),
    'role': os.getenv('SNOWFLAKE_ROLE')  # Optional
}

# Establish the Snowpark session
session = Session.builder.configs(connection_parameters).create()

# Example query using Snowpark
df = session.sql("SELECT CURRENT_USER(), CURRENT_VERSION()")

# Show the results as a DataFrame
df.show()

# You can also collect the results if needed
result = df.collect()
print(result)

# Close the session when done
session.close()
