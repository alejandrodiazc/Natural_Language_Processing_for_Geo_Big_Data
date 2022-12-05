import random
from flask import Blueprint
from flask import request
import requests
import json
import firebase_admin
import time 
from firebase_admin import db

cred = firebase_admin.credentials.Certificate("D:\Escritorio\Descargas\inegi-497e7-firebase-adminsdk-s4h6a-19e076bdc5.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://inegi-497e7-default-rtdb.firebaseio.com/'
	})
ref  = db.reference("/Busqueda1")

API_KEY='eyJpZCI6ImVkYWM0NTBjLTQzNTEtNDZhMC1iNjQ1LTI0MzAwYzVmZDAzYSIsImlhdCI6MTY2ODUzMzk5NH0'

bp = Blueprint("api", __name__)

def request_entities(text):
    url = "https://invoke.neuraan.com/default/v1"
    payload = json.dumps({
        "name": "Custom NER",
        "input": { "text": text},
        "threshold": 0.7})
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    api_response = json.loads(response.text)
    
    if len(api_response["result"]["detected"]) > 0:
        detected = [e[0] for e in api_response["result"]["detected"]]
        return detected, api_response
    return [], api_response

@bp.route("/get-business", methods=("GET", "POST"))
def get_business():
    if request.method == "POST":
        data = json.loads(request.data)
        neuraan_reponse = data["__neuraan_core_response__"]
        #Call custom NER
        entities, api_response = request_entities(neuraan_reponse["query"])
        ref.update({"CodigoNegocio":entities})
        if len(entities) > 0:
            return {'negocios': entities, 'response': entities[0], 'success': True}
        else:
            return {'negocios': entities, 'response': 'No detecté el negocio. Puedes decirlo de nuevo por favor?', 'success': False}

@bp.route("/get-postal-code", methods=("GET", "POST"))
def get_postal_code():
    if request.method == "POST":
        data = json.loads(request.data)
        neuraan_reponse = data["__neuraan_core_response__"]
        negocios = data["negocio"]
        #Call custom NER
        entities, api_response = request_entities(neuraan_reponse["query"])
        #Query database
        ref.update({"CP":entities})
        if len(entities) > 0:
            return {'response': query_database(negocios, entities[0]), 'success': True}
        else:
            return {'response': 'Porfavor proporicone un C.P. válido', 'success': False}

def query_database(business, postal_code):
    time.sleep(30)
    ff = db.reference("/Busqueda1/NumNegocios")
    f1 = db.reference("/Busqueda1/NegociosMas")
    f3 = db.reference("/Busqueda1/NegociosMasNum")
    f2 = db.reference("/Busqueda1/NegociosMenos")
    f4 = db.reference("/Busqueda1/NegociosMenosNum")
    business_number = ff.get()
    business_mas = f1.get()
    business_mas_num = f3.get()
    business_menos = f2.get()
    business_menos_num = f4.get()

    return f"En el codigo postal {postal_code} hay {business_number} {business}. El negocio más popular es {business_mas}, con {business_mas_num} locales. El negocio menos popular es {business_menos}, con {business_menos_num} locales."