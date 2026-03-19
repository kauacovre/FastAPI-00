from fastapi.testclient import TestClient  
from fastapi-zero.app import app  

client = TestClient(app)