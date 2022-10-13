import uvicorn
from app import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
