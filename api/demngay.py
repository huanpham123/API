from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_days():
    start_date = date(2024, 5, 14)
    current_date = date.today()
    delta = current_date - start_date
    
    return jsonify({
        "start_date": start_date.strftime("%d-%m-%Y"),
        "current_date": current_date.strftime("%d-%m-%Y"),
        "days_elapsed": delta.days
    })

# Bắt buộc phải có cho Vercel
handler = app
