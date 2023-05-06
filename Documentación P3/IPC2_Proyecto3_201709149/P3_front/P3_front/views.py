from django.http import HttpResponse
from django.shortcuts import render, redirect

import xml.etree.ElementTree as eT
from . import Reader

reader_obj = Reader.Reader()

def main_view(request):
    contexto = {"nombre": "A-name"}
    return render(request, "P3_front/main_template.html", contexto)

def formXML_view(request):
    #return render(request, "P3_front/xml_form.html", None)

    if request.method == 'POST':
        # Obtener el archivo cargado
        xml_file = request.FILES['xml-file']
        # Crear un objeto ElementTree a partir del archivo cargado
        xml_tree = eT.ElementTree(file=xml_file)
        # Acceder al elemento raíz del archivo XML
        root = xml_tree.getroot()

        # Procesado del XML 1
        reader_obj.process_XML_Sol1(root)

        #return HttpResponse('Archivo cargado exitosamente')
        return redirect('Proyecto 3')
    else:
        print("Se cargó desde el inicio...")
        return render(request, 'xml_form.html')