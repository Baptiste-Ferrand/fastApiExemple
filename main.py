from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base, Item
from database import engine, get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur votre API FastAPI!"}
# Créer les tables au démarrage
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/items/{item_id}")
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await db.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
