from fastapi import FastAPI, Body, Path, Query
from typing import Optional
from pydantic import BaseModel

# initiate app
app = FastAPI()