from flask import Flask, render_template, request, make_response
from routes.rutas import processXMLO

import xml.etree.ElementTree as ET
import os
import xmltodict
import json

from objects import Reader
from objects import ProfilesList
from objects import Profile
from objects import Word
from objects import WordsList
from objects import Writer

reader_obj = Reader.Reader()
writer_obj = Writer.Writer()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Servidor Flask en marcha..."

@app.route('/MandarPerfiles', methods=['POST', 'GET'])
def processXMLsolO():
    print(" *** Cargando información previa...")
    reader_obj.load_from_data_base()    
    # ------------------------------------------------------------------
    print(" *** Se procesará el archivo de la solicitud 1")

    #print(os.getcwd())
    # Recuperación del fichero
    xml_file = request.files.get('xml-file')
    xml_file.save('files/savedSOL-ONE.xml')

    # Carga a elemnto manejable
    tree = ET.parse('files/savedSOL-ONE.xml')
    root = tree.getroot()

    reader_obj.process_XML_Sol1(root)

    writer_obj.write_stored_data_s1(reader_obj.savedProfiles, reader_obj.discartedWords)
    print("------------------------------------------------------------------")

    xml = f'''<respuesta>
            <perfilesNuevos>
                Se han creado {reader_obj.new_profiles_cant} perfiles nuevos
            </perfilesNuevos>
            <perfilesExistentes>
                Se han actualizado {reader_obj.updated_profiles_cant} perfiles existentes
            </perfilesExistentes>
            <descartadas>
                Se han creado {reader_obj.created_d_words} nuevas palabras a descartar
            </descartadas>
        </respuesta>'''

    diccionario = xmltodict.parse(xml)
    json_objeto = json.dumps(diccionario)

    return xml, 200 

@app.route('/ResetData', methods=['POST', 'GET'])
def resetSavedData():
    f = open('files/storedDataService1.xml', 'w')
    f.write('')
    reader_obj = Reader.Reader()
    
    print(" *** SE HA ELIMINADO LA INFORMACIÓN PREVIA")
    return "*** Información eliminada correctamente..."

if __name__ == '__main__':
    app.run(debug=True)