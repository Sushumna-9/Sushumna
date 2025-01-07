from flask import Flask, render_template
from models import fetch_data
from views import render_data

app = Flask(__name__)

@app.route('/')
def home():
    try:
        data = fetch_data()
        return render_data(data)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '_main_':

    app.run(debug=True)