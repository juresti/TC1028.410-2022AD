def deseaContinuar(resp):
    "Solo continua si la respuesta fue 'si'"
    print(resp)
    resp = resp.lower()
    print(resp)
    if (resp == "si"):
        return True
    else:
        return False
    