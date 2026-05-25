from fastapi import FastAPI

import uvicorn 

from users.controller import router as user_router 

app = FastAPI()

app.include_router(router=user_router, prefix="/users")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)