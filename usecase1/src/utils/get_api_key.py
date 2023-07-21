import os

def get_api_key():
    api_key = os.environ.get("MESSAGEBIRD_API_KEY")

    if api_key:
        print("The MESSAGEBIRD_API_KEY environment variable is set.")
    else:
        print("The MESSAGEBIRD_API_KEY environment variable is not set.")

    return api_key