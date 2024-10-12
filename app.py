import uvicorn
import os
from fastapi import FastAPI

app = FastAPI()

port = int(os.getenv("PORT", 5090))
if __name__ == "__main__":
    uvicorn.run(app, port=port, host="0.0.0.0")
