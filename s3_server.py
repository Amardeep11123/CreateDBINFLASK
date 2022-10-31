# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response
import sqlite3
 
# (A2) FLASK SETTINGS + INIT

DBFILE = "market.db"
app = Flask(__name__)
# app.debug = True
 
# (B) HELPER FUNCTION - SEARCH USERS
def getusers(search):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute(
    "SELECT * FROM `menu` WHERE `name` LIKE ? OR `id` LIKE ?",
    ["%"+search+"%", "%"+search+"%"]
  )
  results = cursor.fetchall()
  conn.close()
  return results

def getlist(name):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute(
    "SELECT * FROM `menu` WHERE `name`= ? ",
    [name]
  )
  results = cursor.fetchall()
  conn.close()
  return results

# (C) DEMO SEARCH PAGE
@app.route("/", methods=["GET", "POST"])
def index():
  # (C1) SEARCH FOR USERS
  if request.method == "POST":
    data = dict(request.form)
    users = getusers(data["search"])
  else:
    users = []
 
  # (C2) RENDER HTML PAGE
  return render_template("s4_users.html", usr=users)

@app.route("/test", methods=["GET", "POST"])
def test():
  # (C1) SEARCH FOR USERS
  select = request.form.get('')
 
  # (C2) RENDER HTML PAGE
  return render_template("test.html", select=select)
 
# (D) START
if __name__ == "__main__":
  app.run(debug=True)