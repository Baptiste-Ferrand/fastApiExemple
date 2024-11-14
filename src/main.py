import sys
import os
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import engine
from src.models.user import Base
from src.routes import profile, user, auth
from src.scripts.init_db import create_initial_data

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await create_initial_data()
        yield
    except Exception as e:
        print(f"Erreur pendant l'initialisation de l'application : {e}")
        raise  # Pour arrêter le démarrage si nécessaire

app = FastAPI(lifespan=lifespan)

# Enregistrer les routes
app.include_router(profile.router, prefix="/profile", tags=["profil"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Bienvenue sur votre API FastAPI!"}
