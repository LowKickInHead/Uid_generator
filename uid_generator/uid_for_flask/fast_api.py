import my_module
from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    new = my_module.uid_generate()
    return new

print("тест записи")