# test_client.py
# local PC command: uvicorn server:app --host 0.0.0.0 --port 8000
# local network command: ws://10.150.52.215:8000/ws
# see apis running local command: ps aux | grep uvicorn 

import asyncio
import websockets
import json

async def listen():
    uri = "ws://10.150.52.215:8000/ws"  # Use 'localhost' if running on the same machine
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                vector = data.get("vector", [])
                text = data.get("text", "")
                print(f"Received Vector: {vector}")
                print(f"Received Text: {text}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")

if __name__ == "__main__":
    asyncio.run(listen())
