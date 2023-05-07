from django.http import HttpResponse
from django.shortcuts import render, redirect

import requests
import json
from django.http import JsonResponse
import xml.etree.ElementTree as eT
from io import BytesIO
from django.contrib import messages

def main_view(request):
    contexto = {"nombre": "A-name"}

    return render(request, "P3_front/main_template.html", contexto)

def formXML_view(request):

    if request.method == 'POST':        
        xml_file = request.FILES['xml-file']        
        xml_bytes = xml_file.read()
        
        url = 'http://localhost:5000/MandarPerfiles'
        files = {'xml-file': ('xml-file', BytesIO(xml_bytes), 'application/xml')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            print("Response: ", response.text)
            print("Se obtuvo un código 200.")
            #return HttpResponse('XML procesado y guardado en el servidor backend de Flask')                        
            #return HttpResponse(response.text, content_type="application/json")
            return HttpResponse(response.text, content_type="application/xml")
        else:
            print("Response: ",response.text)
            print("No se ha podido procesar el archivo.")
            return HttpResponse('Error al procesar el archivo', status=400)
        xml_file.close()

        flask_response = response.text

        print("RESPONSE:")
        print(flask_response)
        print("---")
        #return HttpResponse('Archivo cargado exitosamente')
    else:
        print("Se cargó desde el inicio...")
        return render(request, 'xml_form.html')

def reset_view(request):
    url = 'http://localhost:5000/ResetData'
    response = requests.get(url)
    messages.warning(request, 'Este es un mensaje de alerta')
    return redirect('Proyecto 3')
    #return HttpResponse('Información borrada exitosamente')