# virtual environment
1. Open terminal and cd to RTSanalytics
2. Set up: 'py -m venv env'
3. run: 'env/Scripts/activate'
4. install required libraries: 'pip install -r requirements.txt'

# Additional setup steps
- Need to install PostgreSQL
- Need to install psycopg2 module:
    pip install psycopg2
- Create a file named "config.ini" in "/database_tools/sc2/" directory
    with the following format:

START OF config.ini:
[database]
username = your_database_username
password = your_database_password
host = your_database_host
port = 5432
database = your_database_name
END OF config.ini

NOTE: Make sure your username/password combo is the same as the
    credentials you use for your PostgreSQL database and that the
    host is set to "localhost" when running locally and the port
    is always 5432 by default.

# How to run sc2_extractor.py
py -m replay_extraction_tools.sc2.sc2_extractor

# How to run sc2_analyzer.py
py -m data_analysis_tools.sc2.sc2_analyzer

# Running Application for School Project
Requires Windows Machine
1. Install python version 3.12
2. Install and setup flutter (If the application doesn't work it is probably because of this step.)
3. Delete env folder
4. Create virtual environment following above steps
5. Run command from root directory RTSanalytics: 'py -m server_tools.sc2.sc2_server_api'
6. Open a new terminal and cd to RTSanalytics/UI/rts-anaslysis
7. Run command 'flutter run'
8. Select the windows setup


# Using Pytest
To ensure all tests get passed, you must run pytest from the root directory as follows:

Linux:
$/SC2_RTS_Analytics> pytest

Windows:
C:\SC2_RTS_Analytics> pytest

If you do not do this, certain program dependencies will not be included in
the tests, which could cause some tests to fail depending on the current working
directory.

# Running black to reformat code
black "relative\path\to\file.py"