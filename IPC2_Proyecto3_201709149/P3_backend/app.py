from flask import Flask, render_template
from routes.rutas import processXMLO

app = Flask(__name__)
app.register_blueprint(processXMLO)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Servidor Flask en marcha..."

if __name__ == '__main__':
    app.run(debug=True)