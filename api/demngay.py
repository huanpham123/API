from flask import Flask, jsonify
from datetime import date
import os

app = Flask(__name__)

@app.route('/api/days', methods=['GET'])
def get_days():
    start_date = date(2024, 5, 14)
    current_date = date.today()
    delta = current_date - start_date
    
    return jsonify({
        "start_date": start_date.strftime("%d-%m-%Y"),
        "current_date": current_date.strftime("%d-%m-%Y"),
        "days_elapsed": delta.days
    })

if __name__ == '__main__':
    app.run()
