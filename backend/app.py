from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import customers_router, products_router, orders_router
from database import Base, engine

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tessemirete API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(customers_router)
app.include_router(products_router)
app.include_router(orders_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)