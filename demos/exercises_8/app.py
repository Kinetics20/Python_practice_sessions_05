from flask import Flask, render_template, session, redirect, request, jsonify
import hashlib
import hmac
import sqlite3
import subprocess
import threading
import time
import sys

NETWORK_RANGE = '192.168.0.172/24'
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
        log_entries=log_get()
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
        log_add('User logged in')
        return redirect("/", 302)

    return render_template(
        "login.html.j2",
        error="Authentication failed."
    )


@app.route("/logout")
def logout():
    if "logged_in" in session:
        del session["logged_in"]
        log_add('User logged out')
    return redirect("/login", 302)


def init_db():
    con = sqlite3.connect('devices.db')
    cur = con.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS log
                (
                    id
                    INTEGER
                    PRIMARY
                    KEY
                    AUTOINCREMENT,
                    timestamp
                    DATETIME
                    DEFAULT
                    CURRENT_TIMESTAMP,
                    message
                    TEXT
                )
                ''')

    con.commit()


def log_add(msg):
    con = sqlite3.connect('devices.db')
    cur = con.cursor()

    cur.execute('''
                INSERT INTO log (message)
                VALUES (?)
                ''', (msg,)
                )

    con.commit()


def log_get(last=50):
    con = sqlite3.connect('devices.db')
    cur = con.cursor()

    cur.execute('''
                SELECT timestamp, message
                FROM log ORDER BY timestamp DESC LIMIT ?
                ''',
                (last,)
                )

    log_entries = []
    for row in cur.fetchall():
        log_entries.append(row)

    return log_entries


def scan_network():
    output = subprocess.check_output(
        [
            './arp-scan',  '-x',  NETWORK_RANGE
        ]
    )

    active_hosts = []

    text = output.decode()
    for line in text.splitlines():
        columns = line.split('\t')
        ip = columns[0]
        mac = columns[1]
        active_hosts.append((mac, ip))

def scan_worker():
    while True:
        active_hosts = scan_network()
        time.sleep(5)


init_db()
th = threading.Thread(target=scan_worker, daemon=True)
th.start()



if __name__ == "__main__":
    app.run(debug=True)
