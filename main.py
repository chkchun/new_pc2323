import fastapi
import uvicorn

print("Hello fastapi")
api = fastapi.FastAPI()

@api.get("/")
def index():
    return {"msg": "Hello from FastAPI",
            "another msg": ["Hello", "World"]}

#uvicorn.run(api)
#uvicorn.run(api, port=8001, host='127.0.0.1')

uvicorn.run(api, port=6789)