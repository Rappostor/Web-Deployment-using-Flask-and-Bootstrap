from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile-bootstrap.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nama_lengkap = request.form["nama_lengkap"]
        return render_template("form-bootstrap.html", message="Form submitted successfully!")
    return render_template("form-bootstrap.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)