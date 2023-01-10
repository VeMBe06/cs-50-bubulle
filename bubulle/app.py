# Import everything you need

from flask import Flask, render_template, request
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


@app.route("/parameters", methods=["GET", "POST"])
def parameters():
    """Change breathing parameters"""
    if request.method == "POST":
        # If we POST, we update the breathing parameters on CSS with JS

        # Obtain profile that was selected
        profile = request.form.get("profile")
        # Create switch statement to find which profile was chosen
        # Do it by hand bc there's no real switch in python 3
        if profile == "profile1":
            # Create vars for animation-name | animation-duration | profile type
            return render_template("index.html", anim_name="breathe1", anim_dur=6, prof_type="1:2:2")

        elif profile == "profile2":
            return render_template("index.html", anim_name="breathe2", anim_dur=9, prof_type="1:3:3")


        elif profile == "profile3":
            return render_template("index.html", anim_name="breathe3", anim_dur=14, prof_type="5:3:5")

        elif profile == "profile4":
            return render_template("index.html", anim_name="breathe4", anim_dur=17, prof_type="5:4:7")

        else:
            return render_template("index.html", anim_name="breathe3", anim_dur=14, prof_type="5:3:5")
    
    
    else:
        # Else we just render the webpage
        return render_template("parameters.html")




@app.route("/about")
def about():
    """Show a quick explanation of the app"""
    
    return render_template("about.html")

