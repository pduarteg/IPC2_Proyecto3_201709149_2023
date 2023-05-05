from django.http import HttpResponse
from django.shortcuts import render

import xml.etree.ElementTree as eT


def main_view(request):
    contexto = {"nombre": "A-name"}
    return render(request, "P3_front/main_template.html", contexto)

def process_file(request):
    if request.method == 'POST' and request.FILES['xml_file']:
        xml_file = request.FILES['xml_file']
        tree = eT.parse(xml_file)
        root = tree.getroot()
        print("HOLA ???")
        
    return render(request, 'template.html')