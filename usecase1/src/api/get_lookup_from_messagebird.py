from ..utils.logger import get_logger
from fastapi.responses import JSONResponse

log = get_logger()

def get_lookup_from_messagebird(ani_input, client):
    if client is None:
        log.error("MessageBird client is None")

    phone_number = ani_input.ANI

    try:
        lookup = client.lookup(phone_number)
        log.info(lookup)
    except Exception as ex:
        log.error(ex)
        return JSONResponse({
            "errorMessage": "Server has technical issues due to fetching from MessageBird"
        })

    return JSONResponse({
        "countryCode": lookup.countryCode,
        "countryPrefix": lookup.countryPrefix,
        "e164": lookup.formats.e164,
    })