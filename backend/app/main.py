from fastapi import FastAPI

from app.router import hello

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to 4DT912 Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
