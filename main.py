from fastapi import FastAPI, WebSocket, Depends
from database import engine, Base
import models
from routers import router as chat_router
from websockets import ConnectionManager

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Real-Time Chat Application API",
    description="An API for a real-time chat application.",
    version="1.0.0"
)

# Include the router in the app
app.include_router(chat_router, prefix="/api")

# Initialize the connection manager
manager = ConnectionManager()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time chat.
    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        manager.disconnect(websocket)
