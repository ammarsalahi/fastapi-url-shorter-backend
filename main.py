from fastapi import FastAPI
from routers import router
from database import engine,Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def init_db():
    Base.metadata.create_all(bind=engine)

app.include_router(router,prefix='/links')
