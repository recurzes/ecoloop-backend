from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

class CREDENTIALS(BaseModel):
    pass