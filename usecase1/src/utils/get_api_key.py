import os
from ..utils.logger import get_logger

log = get_logger()

def get_api_key():
    api_key = os.environ.get("MESSAGEBIRD_API_KEY")

    if not api_key:
        log.error("The MESSAGEBIRD_API_KEY environment variable is set.")

    return api_key