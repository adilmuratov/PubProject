from fastapi import FastAPI

import uvicorn 

from auth.controller import router as auth_router
from users.controller import router as user_router
from userstyles.controller import router as userstyle_router
from profiles.controller import router as profile_router
from posts.controller import router as post_router
from comments.controller import router as comment_router


app = FastAPI()

app.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
app.include_router(router=user_router, prefix="/users", tags=["Users"])
app.include_router(router=userstyle_router, prefix="/userstyles", tags=["Userstyles"])
app.include_router(router=profile_router, prefix="/profiles", tags=["Profiles"])
app.include_router(router=post_router, prefix="/posts", tags=["Posts"])
app.include_router(router=comment_router, prefix="/comments", tags=["Comments"])


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
