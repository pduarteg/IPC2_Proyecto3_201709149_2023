from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

import xml.etree.ElementTree as eT

def main_view(request):
    contexto = {"nombre": "A-name"}
    return render(request, "P3_front/main_template.html", contexto)

def formXML_view(request):

    if request.method == 'POST':        
        xml_file = request.FILES['xml-file']        
        xml_tree = eT.ElementTree(file=xml_file)
        print("Imprimiendo el xml:")
        print(xml_file.read())
        root = xml_tree.getroot()
        xml_file.close()

        url = 'http://localhost:5000/MandarPerfiles'
        files = {'xml-file': xml_tree}
        response = requests.post(url, files=files)
        print(response.status_code)
        if response.status_code == 200:
            return HttpResponse('XML procesado y guardado en el servidor backend de Flask')
        else:
            print("No se ha podido procesar el archivo.")
        # Obtener la respuesta de Flask

        flask_response = response.text

        print("RESPONSE:")
        print(flask_response)
        print("---")
        #return HttpResponse('Archivo cargado exitosamente')
        #return redirect('Proyecto 3')
    else:
        print("Se cargó desde el inicio...")
        return render(request, 'xml_form.html')