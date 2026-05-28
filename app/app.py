from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/health')
def health():
    return {'status': 'ok', 'mensaje': 'Aplicacion corriendo correctamente'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)