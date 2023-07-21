from messagebird import Client as messagebird_client
from fastapi import FastAPI

from .api.get_lookup_from_messagebird import get_lookup_from_messagebird
from .utils.get_api_key import get_api_key
from ..classes.ANIPhoneNumber import ANIPhoneNumber

app = FastAPI()
api_key = get_api_key()
client = messagebird_client(api_key)

@app.post("/get_phone_details/")
def get_phone_details(ani_input: ANIPhoneNumber)-> dict:
    """
    Get phone details from MessageBird.

    This endpoint takes an ANIPhoneNumber object with an 'ANI' field (int) representing the phone number.
    It returns the lookup details obtained from the MessageBird API.

    Parameters:
        - ani_input: ANIPhoneNumber object with the 'ANI' field (int) representing the phone number.

    Returns:
        - dict: A JSON object containing countryCode, countryPrefix and e164.
    """
    return get_lookup_from_messagebird(ani_input, client)

