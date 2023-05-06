from flask import Blueprint, jsonify
from controllers.controller import *

# ejemplo = Blueprint("ejemplo", __name__)

# @ejemplo.route("/ejemplo", methods=['GET'])
# def UnSaludo():
# 	variable = process_xml()
# 	print(variable)
# 	return jsonify(process_xml())

processXMLO = Blueprint("processXMLO", __name__)

@processXMLO.route("/solOne", methods=['GET'])
def processSol1():
	variable = processSolOne()
	print(variable)
	return jsonify(processSolOne())