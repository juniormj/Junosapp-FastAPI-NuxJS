def search_word(output, word, index):
    try:
        finded = output.split().index(word)
        finded = output.split()[finded + index]
    except ValueError:
        finded = ""
    return finded


def get_plan(output, word, index):
    try:
        finded = output.split().index(word)
        finded = output.split()[finded + index]
        finded = finded.split("-")[0]
    except ValueError:
        finded = ""
    return finded


def get_uptime(output):
    try:
        UPTIME_INDEX = output.split().index("uptime:")
        UPTIME = output.split()[UPTIME_INDEX + 1]

        if UPTIME.split(":")[0] in "00":
            UPTIME = f"{UPTIME.split(':')[1]} min"
        elif UPTIME.split(":")[0] not in "00":
            UPTIME2 = output.split()[UPTIME_INDEX + 2]
            UPTIME = f"{UPTIME} {UPTIME2}min"
    except ValueError:
        UPTIME = ""
    return UPTIME


def filtra_xml(xml, str_busca):
    return xml.xpath(str_busca)[0].text[0] + "." + xml.xpath(str_busca)[0].text[1::]


def format_ping(xml, id, ip):
    return (
        f"{xml.xpath('.//response-size')[id].text} bytes from "
        f"{ip}: icmp_seq={xml.xpath('.//probe-index')[id].text} "
        f"ttl={xml.xpath('.//time-to-live')[id].text} time="
        f"{xml.xpath('.//rtt')[id].text[0]}."
        f"{xml.xpath('.//rtt')[id].text[1::]}\n"
    )
