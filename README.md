# CortexSearchDemo
Cortex Search enables low-latency, high-quality “fuzzy” search over your Snowflake data. Cortex Search powers a broad array of search experiences for Snowflake users including Retrieval Augmented Generation (RAG) applications leveraging Large Language Models (LLMs).


STEP 1: Run Snowflakesetup to create a Cortex Search Service.

STEP 2: Validate connection to snowflake from th windows operating envt using a python script (SnowflakeConnectionTest1.py) from Anaconda prompt
    Environment Variables:
      Add the following environment variables to your GitLab CI/CD environment settings or as a .env file:
      
      SNOWFLAKE_USER
      SNOWFLAKE_PASSWORD
      SNOWFLAKE_ACCOUNT
      SNOWFLAKE_WAREHOUSE
      SNOWFLAKE_DATABASE
      SNOWFLAKE_SCHEMA
      SNOWFLAKE_ROLE (if required)

STEP 3: Create a conda envt and install necessary packages from Anaconda prompt
--created a conda demosnowparkdemo in version python 3.8
conda create --name demosnowparkdemo --override-channels -c https://repo.anaconda.com/pkgs/snowflake python=3.8 

pip install snowflake -U
**do not separate install snowpark, connector etc..above will take care of everything
**installed jupyterlab, but could not execute via the kernal demosnowparkdemo, as it was still pointing to python 3.12


STEP 4: Run the CortextFetchService.py from Anaconda prompt
conda activate demosnowparkdemo
python CortextFetchService.py

#################################################
connection_parameters = {
    'account': 'lrpssuw-wp85623',
    'user': 'RAMBASKAR2024',
    'password': 'IXXX!yxxy',
    'warehouse': 'SMALL_WH_CORTEX',
    'database': 'CORTEX_DEMO',
    'schema': 'CORTEX_DEMO_SCH',
    'role': 'CORTEX_DEMO_ROLE'  # Optional
}
################################################
