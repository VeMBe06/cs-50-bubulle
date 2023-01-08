# Import everything you need

from flask import Flask, redirect, render_template, request
from flask_session import Session

# Configure app
app = Flask(__name__)

# Make templates reload automatically (flask only reloads .py files only by default)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Enable debug mode
if __name__ == "__main__":
    app.run(debug = True)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




@app.route("/")
def index():
    """Show the main screen with bubble"""

    return render_template("index.html")

@app.route("/parameters")
def parameters():
    """Change breathing parameters"""
    if request.method == "POST":
        # If we POST, we update the breathing parameters on CSS with JS
        
        return
    
    else:
        # Else we just render the webpage
        return render_template("parameters.html")




@app.route("/theme")
def theme():
    """Change theme"""
    
    return render_template("theme.html")



@app.route("/about")
def about():
    """Show a quick explanation of the app"""
    
    return render_template("about.html")

