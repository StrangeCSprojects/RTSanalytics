"""
    This is a python script used for easier
    debugging, testing, and experimenting
"""

# Import any needed modules
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains on all routes
@app.route('/getPythonFunctionOutput')
def get_output():
    # Assuming the percentage calculation is correct
    percentage = 46.0  # Or your actual dynamic calculation
    return jsonify({'percentage': percentage})

def main():
    """
    Main entry point
    """
    print("Implementing build order database.")

# Interpret this module
if __name__ == "__main__":
    app.run(debug=True, port=5001)
