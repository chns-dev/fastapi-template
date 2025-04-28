from pydantic import BaseModel, ConfigDict

class SimpleSchema(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    message: str
    