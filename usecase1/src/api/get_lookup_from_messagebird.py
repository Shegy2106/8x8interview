from fastapi.responses import JSONResponse

def get_lookup_from_messagebird(ani_input, client):
    phone_number = ani_input.ANI

    lookup = client.lookup(phone_number)

    return JSONResponse({
        "countryCode": lookup.countryCode,
        "countryPrefix": lookup.countryPrefix,
        "e164": lookup.formats.e164,
    })