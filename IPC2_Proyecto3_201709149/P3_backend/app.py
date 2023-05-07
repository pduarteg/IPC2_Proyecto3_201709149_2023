from flask import Flask, render_template
from routes.rutas import processXMLO

import xml.etree.ElementTree as ET

from objects import Reader
from objects import ProfilesList
from objects import Profile
from objects import Word
from objects import WordsList

reader_obj = Reader.Reader()




app = Flask(__name__)
app.register_blueprint(processXMLO)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Servidor Flask en marcha..."

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/MandarPerfiles', methods=['POST', 'GET'])
def processXMLsolO():
    print("------------------------------------------------------------------")
    print("Se procesará el archivo de la solicitud 1")
    xml_file = request.files.get('xml-file')
    xml_file.save('/files/savedSOL-ONE.xml')
    tree = ET.parse('/files/savedSOL-ONE.xml')
    root = tree.getroot()

    reader_obj.process_XML_Sol1(root)
    print(" ESTÁ OCURRIOEN ÉSTO?")

    return "Archivo procesado exitosamente", 200 