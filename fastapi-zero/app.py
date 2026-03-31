from fastapi import FastAPI

app = FastAPI()

def minha_primeira_funcao():
    print("Testando função em python")

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
