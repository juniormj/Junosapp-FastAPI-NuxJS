import sys

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError


async def operation_command(device, command):
    dev = Device(
        host=device,
        user="messias",
        password="Junior@2512",
        normalize=True,
        dev_timeout=55,
    )
    try:
        dev.open()
    except ConnectError as err:
        print(f"Nao pode conectar ao dispositivo: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"O seguinte erro ocorreu: {err}")
        sys.exit(1)
    output = dev.cli(command)
    dev.close()
    return output


async def command_ping(device, ip):
    dev = Device(
        host=device,
        user="messias",
        password="Junior@2512",
        normalize=True,
        dev_timeout=55,
    )
    try:
        dev.open()
    except ConnectError as err:
        print(f"Nao pode conectar ao dispositivo: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"O seguinte erro ocorreu: {err}")
        sys.exit(1)
    output = dev.rpc.ping(count="5", host=ip)
    dev.close()
    return output
