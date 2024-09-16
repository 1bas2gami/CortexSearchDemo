# Fetch service from Snowflake

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
root = Root(session)

# Define and use the Cortex Search service
transcript_search_service = (root
  .databases["CORTEX_DEMO"]
  .schemas["PUBLIC"]
  .cortex_search_services["transcript_search_service"]
)

# Perform search query
resp = transcript_search_service.search(
  query="internet issues",
  columns=["transcript_text", "region"],
  filter={"@eq": {"region": "North America"} },
  limit=1
)

# Print the search result in JSON format
print(resp.to_json())

# Close the session when done
session.close()
