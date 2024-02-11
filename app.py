from flask import Flask
app = Flask(__name__)

# Dictionary to store maintenance logs
maintenance_logs = {
    'PC': [],
    'Printers': [],
    'Equipment': []
}

# Function to log maintenance
def log_maintenance(category, description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    maintenance_logs[category].append({'timestamp': timestamp, 'description': description})

# Routes
@app.route('/')
def index():
    return render_template('index.html', logs=maintenance_logs)

@app.route('/log_maintenance', methods=['POST'])
def log_maintenance_route():
    category = request.form['category']
    description = request.form['description']
    log_maintenance(category, description)
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)