# pip install mysql-connector-python

from flask import Flask, render_template
from markupsafe import escape
import mysql.connector
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "<p>Here is the Index page</p>"

@app.route("/data", methods=["GET"], strict_slashes=False)
def data():
    
    connection = mysql.connector.connect(host="localhost",
                                     port="3306",
                                     database="summarizer",
                                     user="root",
                                     password="Gisprog_1")
    
    selectQuery = "SELECT * FROM summary WHERE user_id = 1"

    cursor = connection.cursor()
    cursor.execute(selectQuery)
    rows = cursor.fetchall()

    row_list = []

    if cursor.rowcount == 0:
        # Create empty object to ensure returned list has at least one entry.
        row_list.append({"created_date":"", \
                         "article_text":"", \
                         "article_url":"", \
                         "summary_text":"", \
                         "summary_length":0})
    else:
        for row in rows:
            # Check columns that accept null values and set to non-null.
            article_text = row[2]
            if article_text == None:
                article_text = ""
            article_url = row[3]
            if article_url == None:
                article_url = ""
            summary_length = row[5]
            if summary_length == None:
                summary_length = 0
            # Format date column.
            date_string = f"{row[1]:%Y-%m-%d}"
            # Create json format object for current row and append to the list.
            row_list.append({"created_date":date_string, \
                             "article_text":article_text, \
                             "article_url":article_url, \
                             "summary_text":row[4], \
                             "summary_length":summary_length})

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    # Return the data for the identified user.
    return row_list

@app.route("/welcome")
def welcome():
    return f"Welcome to my app!"

@app.route("/<name>")
def welcome_name(name):
    return f"Welcome, {escape(name)}!"

if __name__ == "__main__":
    app.run()
