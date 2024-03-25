from flask import Flask, request

app = Flask(__name__)

logs = {}

@app.route('/log', methods=['POST'])
def log():
    log_data = request.form.to_dict()
    service_name = log_data.get('service')
    if service_name not in logs:
        logs[service_name] = []
    logs[service_name].append(log_data.get('message'))
    return 'Log received successfully', 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return logs

if __name__ == '__main__':
    app.run()