from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    config_value = os.getenv('CONFIG_VALUE', 'Default Config')
    db_username = os.getenv('DB_USERNAME', 'Default User')
    db_password = os.getenv('DB_PASSWORD', 'Default Password')
    return f"Config Value: {config_value}, DB Username: {db_username}, DB Password: {db_password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)