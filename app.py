from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Create or append to a log file named after today's date
    log_filename = f"{date_str}.txt"
    log_entry = f"{date_str} {time_str}\n"

    with open(log_filename, "a") as log_file:
        log_file.write(log_entry)

    # Pass current datetime to HTML
    return render_template('index.html', current_date=date_str, current_time=time_str)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
