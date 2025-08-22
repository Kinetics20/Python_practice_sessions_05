from flask import Flask, render_template, session, redirect, request, jsonify
import hashlib
import hmac
import sqlite3

app = Flask(__name__)
app.static_folder = "static"
app.template_folder = "templates"
app.jinja_env.autoescape = True
app.secret_key = "mwie-9jf-92=93u-9j2ff-923j9fj-9j2f9j2f"

@app.route("/")
@app.route("/index.html")
def index():
    if not session.get("logged_in"):
        return redirect("/login", 302)

    return render_template(
        "index.html.j2",

    )

@app.route("/log")
def view_log():
    if not session.get("logged_in"):
        return redirect("/login", 302)

    return render_template(
        "log.html.j2",
        log_entries = [
            ("2025-08-14", "STH"),
            ("2025-08-14", "HOME"),
        ]
    )

@app.route("/api/get-devices")
def get_devices():
    return jsonify([
        {
            "last_ip": "127.0.0.1",
            "mac": "AA:BB:CC:DD:EE:FF",
            "last_seen": "2025-07-22 20:31:00",
            "last_scan_results": "Scan was positive"
        },
        {
            "last_ip": "127.0.0.2",
            "mac": "AA:BB:CC:DD:EE:FF",
            "last_seen": "2025-07-22 20:31:00",
            "last_scan_results": "Scan was positive"
        }
    ])

@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html.j2")

@app.route("/login", methods=["POST"])
def login_post():
    passwd = request.form.get("password")

    HASH = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'

    if hmac.compare_digest(hashlib.sha256(passwd.encode()).hexdigest(), HASH):
        session["logged_in"] = True
        return redirect("/", 302)

    return render_template(
        "login.html.j2",
        error="Authentication failed."
    )

@app.route("/logout")
def logout():
    if "logged_in" in session:
        del session["logged_in"]
    return redirect("/login", 302)



if __name__ == "__main__":
    app.run(debug=True)