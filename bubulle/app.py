# Import everything you need

from flask import Flask, redirect, render_template

# Configure app
app = Flask(__name__)

# Make templates reload automatically (flask only reloads .py files only by default)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Enable debug mode
if __name__ == "__main__":
    app.run(debug = True)

@app.route("/")
def index():
    """Show the main screen wiht bubble"""

    return render_template("index.html")

