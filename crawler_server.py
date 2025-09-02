import time
import json
import threading
from flask import Flask, render_template, jsonify
from crawler import plot_info as plot_data, crawl

# --- Global data storage (shared between threads) ---
# Use a lock to prevent race conditions when updating the list
data_lock = threading.Lock()

# --- Flask Web Server ---
app = Flask(__name__)

# This route serves the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# This route provides the data to the chart
@app.route('/data')
def get_data():
    with data_lock:
        return jsonify(plot_data)

if __name__ == "__main__":
    # Start the crawler in a separate thread
    crawler_thread = threading.Thread(target=crawl, args=(data_lock,), daemon=True)
    crawler_thread.start()
    
    # Run the Flask web server
    # use_reloader=False is important to prevent running the crawler twice
    app.run(debug=True, use_reloader=False, port=5001)