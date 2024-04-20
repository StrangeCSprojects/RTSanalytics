"""
    This is a python script used for easier
    debugging, testing, and experimenting
"""

# Import any needed modules
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/getPythonFunctionOutput")
def get_output():
    # Your Python function
    output = {"data": f"{46}%"}
    return jsonify(output)


def main():
    """
    Main entry point
    """
    print("Implementing build order database.")


# Interpret this module
if __name__ == "__main__":
    app.run(debug=True, port=5001)
