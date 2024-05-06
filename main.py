from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root_route():
    return {'Fast API': 'Todo App'}