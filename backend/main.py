from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from config import settings

from auth.routes import auth_router
from posts.routes import posts_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(settings.MAIN_URL)
async def root():
    return {"message": "Hello World"}

app.include_router(auth_router, prefix='/auth')
app.include_router(posts_router, prefix='/posts')

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)