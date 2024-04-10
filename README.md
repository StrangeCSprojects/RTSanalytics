# virtual environment
1. Set up: py -m venv env
2. run: env/Scripts/activate
3. install required libraries: pip install -r requirements.txt

# Additional setup steps
- Need to add a 'data' folder under database_tools

# How to run sc2_extractor.py
py -m replay_extraction_tools.sc2_extractor

# How to run sc2_analyzer.py
py -m data_analysis_tools.sc2.sc2_analyzer

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