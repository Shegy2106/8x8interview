from pydantic import BaseModel

class ANIPhoneNumber(BaseModel):
    ANI: int