from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/api/days', methods=['GET'])
def get_days():
    # Ngày bắt đầu: 14/05/2024
    start_date = date(2024, 5, 14)
    current_date = date.today()
    delta = current_date - start_date
    return jsonify({
        "start_date": start_date.strftime("%Y-%m-%d"),
        "current_date": current_date.strftime("%Y-%m-%d"),
        "days_elapsed": delta.days
    })

# Dòng dưới giúp chạy ứng dụng cục bộ khi test
if __name__ == '__main__':
    app.run(debug=True)
