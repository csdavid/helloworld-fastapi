from fastapi import FastAPI

app = FastAPI()


@app.get("/greet/{name}")
def saludo(name: str):
    return {"message": f"Hello {name}"}
