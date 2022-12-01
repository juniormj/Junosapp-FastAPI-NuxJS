from typing import List

from config import setting
from models.bras_model import BrasModel
from schemas.bras_schema import BrasSchemaBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from .filter import filtra_xml, format_ping, get_plan, search_word
from .system_bras import command_ping, operation_command
from .utils import scanner_ip, verify_port


async def get_initial(login: str) -> dict:
    ips_olt: List[str] = []
    bras: List[BrasSchemaBase]
    engine = create_async_engine(setting.SQLALCHEMY_DATABASE_URI)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            query = select(BrasModel)
            result = await session.execute(query)
            bras = result.scalars().unique().all()

            print(bras)

    [ips_olt.append(i.ip) for i in bras]

    command = f"show subscribers user-name {login} extensive"

    for ip_olt in ips_olt:

        generic = await operation_command(ip_olt, command)
        if len(generic) > 50:

            LOGIN = search_word(generic, "Name:", 1)
            IP = search_word(generic, "IP", 2)
            PREFIPv6 = search_word(generic, "Prefix:", 1)
            VLAN = search_word(generic, "VLAN", 2)
            PLANO = get_plan(generic, "junos-output-filter:", 1)
            INTERFACE = search_word(generic, "Interface:", 1)

            return {
                "login": LOGIN,
                "ip": IP,
                "prefipv6": PREFIPv6,
                "vlan": VLAN,
                "plano": PLANO,
                "interface": INTERFACE,
                "ip_olt": ip_olt,
            }


async def get_vlan_total(vlan: str, ip_olt: str) -> dict:
    command = f"show subscribers client-type pppoe vlan-id {vlan} count"
    output = await operation_command(ip_olt, command)
    result = output.split()[5]
    return {"total_conn_vlan": result}


async def get_total_client(ip_olt: str) -> dict:
    output = await operation_command(ip_olt, "show subscribers summary")
    result = search_word(output, "PPPoE:", 1)
    return {"total_client": result}


async def get_ports(ip: str) -> dict:
    ports = scanner_ip(ip)
    try:
        list_ports = verify_port(ports)
        PORTA_ONU = list_ports[0]
        PORTA_ROUTER = list_ports[1]
    except:
        PORTA_ONU = 0
        PORTA_ROUTER = 0

    return {"porta_onu": PORTA_ONU, "porta_router": PORTA_ROUTER}


async def get_logout(login: str, ip_olt: str) -> str:
    command = f"clear network-access aaa subscriber username {login}"
    disconnect = await operation_command(ip_olt, command)
    if "not found" in disconnect:
        return f"O usuário {login} não foi encontrado !!!"
    return f"O usuário {login} foi desconectado com sucesso !!!"


async def get_ping_test(ip: str) -> dict:
    xmldata = await command_ping("172.19.255.45", ip)

    packet = xmldata.xpath(".//packet-size")[0].text
    transmitido = xmldata.xpath(".//probes-sent")[0].text
    recebido = xmldata.xpath(".//responses-received")[0].text
    perdido = xmldata.xpath(".//packet-loss")[0].text

    if recebido != "0":

        minimo = filtra_xml(xmldata, ".//rtt-minimum")
        medio = filtra_xml(xmldata, ".//rtt-average")
        maximo = filtra_xml(xmldata, ".//rtt-maximum")
        padrao = filtra_xml(xmldata, ".//rtt-stddev")

        ping = format_ping(xmldata, 0, ip)
        ping += format_ping(xmldata, 1, ip)
        ping += format_ping(xmldata, 2, ip)
        ping += format_ping(xmldata, 3, ip)
        ping += format_ping(xmldata, 4, ip)
        ping += f"\n--- {ip} ping statistics ---\n"
        ping += f"{transmitido} packets transmitted, " f"{recebido} packets received, " f"{perdido}% packet loss\n"
        ping += f"round-trip min/avg/max/stddev = " f"{minimo}/{medio}/{maximo}/{padrao} ms"
    else:
        ping = f"\n--- {ip} ping statistics ---\n"
        ping += f"{transmitido} packets transmitted, " f"{recebido} packets received, {perdido}" f"% packet loss\n"

    return {"ping": ping, "ip": ip, "packet": packet}


async def get_extensives(login: str, ip_olt: str) -> dict:

    command = f"show subscribers user-name {login} extensive"
    extensive = await operation_command(ip_olt, command)

    return {"extensive": extensive}


async def get_update_traffic(interface: str, ip_olt: str) -> dict:
    DOWN_IPv4: int = 0
    DOWN_IPv4: int = 0
    UP_IPv4: int = 0
    UP_IPv6: int = 0
    DOWN_IPv6: int = 0
    DOWN_TOTAL: int = 0
    UP_TOTAL: int = 0
    command = f"show interfaces {interface} extensive"

    output_com = await operation_command(ip_olt, command)

    traf_ipv4 = [i for i, n in enumerate(output_com.split()) if n == "statistics:"]

    if len(traf_ipv4) == 3:
        index_traf = traf_ipv4[-1]

        UP_IPv4 = str(output_com).split()[index_traf + 5]
        DOWN_IPv4 = str(output_com).split()[index_traf + 11]
        UP_IPv6 = 0
        DOWN_IPv6 = 0
        down_tl_int = int(DOWN_IPv4) + int(DOWN_IPv6)
        DOWN_TOTAL = str(down_tl_int)

        up_tl_int = int(UP_IPv4) + int(UP_IPv6)
        UP_TOTAL = str(up_tl_int)

    elif len(traf_ipv4) == 5:
        index_traf = traf_ipv4[-2]
        index_traf6 = traf_ipv4[-1]

        UP_IPv4 = str(output_com).split()[index_traf + 5]
        DOWN_IPv4 = str(output_com).split()[index_traf + 11]

        BPS_UP6 = str(output_com).split()[index_traf6 + 6]
        BPS_DOWN6 = str(output_com).split()[index_traf6 + 12]

        if BPS_UP6 == "bps":
            UP_IPv6 = str(output_com).split()[index_traf6 + 5]
        else:
            UP_IPv6 = 0

        if BPS_DOWN6 == "bps":
            DOWN_IPv6 = str(output_com).split()[index_traf6 + 11]
        else:
            DOWN_IPv6 = 0

        down_tl_int = int(DOWN_IPv4) + int(DOWN_IPv6)
        DOWN_TOTAL = str(down_tl_int)

        up_tl_int = int(UP_IPv4) + int(UP_IPv6)
        UP_TOTAL = str(up_tl_int)

    return {
        "DOWN_IPv4": DOWN_IPv4,
        "UP_IPv4": UP_IPv4,
        "DOWN_IPv6": DOWN_IPv6,
        "UP_IPv6": UP_IPv6,
        "DOWN_TOTAL": DOWN_TOTAL,
        "UP_TOTAL": UP_TOTAL,
    }
