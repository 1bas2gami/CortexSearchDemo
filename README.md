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

STEP 3: Create a conda envt and install necessary packages from Anaconda prompt/power shell
--created a conda demosnowparkdemo in version python 3.8
conda create --name demosnowparkdemo --override-channels -c https://repo.anaconda.com/pkgs/snowflake python=3.8 

pip install snowflake -U
**do not separate install snowpark, connector etc..above will take care of everything
**installed jupyterlab, but could not execute via the kernal demosnowparkdemo, as it was still pointing to python 3.12


STEP 4: Clone the code in VSS from gitlab
4.1 create folder C:\Users\ramba\Baskar\TechProjects\CortexSearchDemo
4.2 git clone https://github.com/1bas2gami/CortexSearchDemo.git
4.3 open VSS and switch to folder git clone https://github.com/1bas2gami/CortexSearchDemo.git
4.4 setup and activate conda

To activate a Conda environment from Visual Studio Code (VS Code), follow these steps:        
        1. Ensure Conda is installed: (STEP 3)
        If you haven’t installed Conda, download and install Anaconda or Miniconda first.
        
        2. Install Python Extension for VS Code:
        Open VS Code.
        Go to the Extensions view by clicking on the Extensions icon on the sidebar or pressing Ctrl + Shift + X.
        Search for Python and install the official extension by Microsoft.
        
        3. Create or Activate a Conda Environment:
        Open a terminal in VS Code by pressing Ctrl + ` .
        If you already have a Conda environment, you can activate it with:
        bash        
        conda activate <your_environment_name>
        
        To create a new Conda environment, use:
        bash        
        conda create --name <your_environment_name> python=3.x        
        conda activate <your_environment_name>
        
        4. Select the Conda Environment in VS Code:
        After activating the Conda environment in the terminal, VS Code might not automatically detect it. To ensure VS Code uses the Conda environment:

        Press Ctrl + Shift + P to open the Command Palette.
        Type Python: Select Interpreter and choose the environment you want to use.
        You should see your Conda environment listed here, with the name of your environment. Select it.
        
        5. Verify Environment Activation:
        After selecting the Conda environment, the terminal will show the environment name in parentheses before the directory path, confirming activation.
        You can also run the following command in the terminal to check the active Python interpreter:
        bass
        python --version

      
        6. Run the CortextFetchService.py from VSS/execute python code button         
        
        #conda activate demosnowparkdemo --not needed since selected from above vss step
        python CortextFetchService.py --if running from vss command prompt

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
