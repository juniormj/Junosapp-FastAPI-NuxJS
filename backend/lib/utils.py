import json
import socket
import sys
from typing import List

import requests
from config import setting
from fastapi import status
from fastapi.exceptions import HTTPException

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"


def verify_port(ports: List[int]):
    list_ports: List[int] = []
    PORTA_ONU: int = 0
    PORTA_ROUTER: int = 0

    ionu = [i for i in ports if i == 80 or i == 443 or i == 50320]
    try:
        PORTA_ONU = ionu[0]
    except IndexError:
        PORTA_ONU = 0
    list_ports.append(PORTA_ONU)
    irouter = [i for i in ports if i == 50330]
    try:
        PORTA_ROUTER = irouter[0]
    except IndexError:
        PORTA_ROUTER = 0
    list_ports.append(PORTA_ROUTER)

    return list_ports


def scanner_ip(ip, sh_ports_closed=0):
    open_ports: List[int] = []

    ports: List[int] = [80, 50320, 50330]

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            else:
                if sh_ports_closed > 0:
                    print(f" {port}")
            sock.close()
    except KeyboardInterrupt:
        print("Você pressionou <Ctrl>+<C>")
        sys.exit()

    except socket.gaierror:
        print("O hostname não pode ser resolvido")
        sys.exit()

    except socket.error:
        print("Não foi possível conectar no servidor")
        sys.exit()
    return open_ports


async def get_log() -> dict:
    topsapp = setting.IP_TOPSAPP

    files = {
        "usuario": (None, setting.USER_TOPSAPP),
        "senha": (None, setting.PASS_TOPSAPP),
        "identificador": (None, setting.ID_TOPSAPP),
    }

    r = requests.post("https://" + topsapp + ":9910/Login", files=files, verify=False)

    files = {
        "idUsuario": (None, r.json()["id_usuario"]),
        "sessao": (None, r.json()["sessao"]),
        "identificador": (None, setting.ID_TOPSAPP),
    }

    logs = requests.post(f"https://{topsapp}:9910/ObterLogsRadius", files=files, verify=False)

    # faz logoff da API
    requests.post(f"https://{topsapp}:9910/Logout", files=files, verify=False)
    return json.loads(logs.text)


async def get_log_login(login: str) -> dict:
    logs: dict = await get_log()
    try:
        return dict([i for i in logs.items() if login in i[1]])
    except:
        raise HTTPException(detail=f"Não foi possivel encontrar log de {login}", status_code=status.HTTP_204_NO_CONTENT)


async def get_obter_clientes_servicos(login: str) -> dict:
    topsapp = setting.IP_TOPSAPP

    files = {
        "usuario": (None, setting.USER_TOPSAPP),
        "senha": (None, setting.PASS_TOPSAPP),
        "identificador": (None, setting.ID_TOPSAPP),
    }

    r = requests.post(f"https://{topsapp}:9910/Login", files=files, verify=False)

    files = {
        "idUsuario": (None, r.json()["id_usuario"]),
        "sessao": (None, r.json()["sessao"]),
        "identificador": (None, setting.ID_TOPSAPP),
        "usuario": (None, login),
    }

    output = requests.post(f"https://{topsapp}:9910/ObterClientesServicos", files=files, verify=False)

    # faz logoff da API
    requests.post(f"https://{topsapp}:9910/Logout", files=files, verify=False)
    return json.loads(output.text)


async def get_obter_suporte_cliente(id_cliente: int) -> dict:
    topsapp = "179.108.49.238"

    files = {
        "usuario": (None, setting.USER_TOPSAPP),
        "senha": (None, setting.PASS_TOPSAPP),
        "identificador": (None, setting.ID_TOPSAPP),
    }

    r = requests.post(f"https://{topsapp}:9910/Login", files=files, verify=False)

    files = {
        "idUsuario": (None, r.json()["id_usuario"]),
        "sessao": (None, r.json()["sessao"]),
        "identificador": (None, setting.ID_TOPSAPP),
        "idCliente": (None, id_cliente),
        "ordenarRegra": (None, "1"),
        "ordenarTipo": (None, "1"),
        "status": (None, "1"),
    }

    output = requests.post(f"https://{topsapp}:9910/ObterSuporte", files=files, verify=False)

    # faz logoff da API
    requests.post(f"https://{topsapp}:9910/Logout", files=files, verify=False)
    return json.loads(output.text)
