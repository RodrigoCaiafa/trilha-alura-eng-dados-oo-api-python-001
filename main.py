
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from constantes import *
from collections import defaultdict
import requests
import os

app = FastAPI()

def _load_base_api(api_base: str) -> str | None:
    load_dotenv()
    API_BASE = os.getenv(api_base)
    return API_BASE

def _response_api(base_api: str, end_point: str) -> requests.Response:
    response = requests.get(f'{base_api}{end_point}')
    return response

def _verif_config_api(base_api: str, end_point: str) -> str:
    if not isinstance(base_api, str) or not isinstance(end_point, str):
        raise TypeError('Endereços precisam ser strings')
    if not base_api.strip() or not end_point.strip():
        raise TypeError('Endereços não podem ser vazios')
    return f'{base_api}{end_point}'

def _json_response_api(obj: dict | list, type_content = 'application/json', encoding = 'utf-8'):
    return JSONResponse(content=obj,
                        headers={"Content-Type": f'{type_content}; charset={encoding}'})

@app.get('/api/hello')
def get_hello_world() -> dict:
    '''
    Endpoint de boas vindas ao mundo API
    :return: dict
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint de busca dos cardapios de restaurantes
    :param restaurante: str -> Nome do restaurante a localizar
    :return: None
    '''

    BASE_API = _load_base_api('API_RESTAURANTE_URL')
    URL = _verif_config_api(BASE_API, CARDAPIO_ENDPOINT)
    response = requests.get(URL)

    get_response = response.json() if response.status_code == 200 else {'NÁO ENCONTRADO':None}

    if restaurante is None:
        return _json_response_api(obj=get_response)

    busca_restaurante = defaultdict(list)

    for item in get_response:
        if item.get('Company') == restaurante:
            busca_restaurante[item.get(restaurante)].append(
                {'nome': item.get('Item'),
                 'descricao': item.get('description'),
                 'preco': item.get('price')})

    return _json_response_api(obj={'Restaurante': restaurante, 'Cardápio': busca_restaurante})


