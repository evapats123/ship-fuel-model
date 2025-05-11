import asyncio
import websockets
import json
import csv
import os
from datetime import datetime

# 🔑 Replace with your actual API key from https://aisstream.io/apikeys
API_KEY = "4c5d94980f5d48d77f77eb84aff62fed43fe1594"

# 📁 Save CSV to the data folder relative to this file
CSV_FILE = os.path.join(os.path.dirname(__file__), "../data/ais_stream_output.csv")

# 💾 Column headers for CSV output
HEADERS = [
    "timestamp", "mmsi", "latitude", "longitude",
    "sog", "cog", "true_heading", "navigational_status"
]

async def connect_and_stream():
    uri = "wss://stream.aisstream.io/v0/stream"

    try:
        async with websockets.connect(uri) as websocket:
            # Define your subscription
            subscription = {
                "APIKey": API_KEY,
                "BoundingBoxes": [[[33.72, -118.28], [33.97, -118.15]]],  # Port of LA
                "FilterMessageTypes": ["PositionReport"]
            }

            await websocket.send(json.dumps(subscription))

            # Open CSV file for writing
            with open(CSV_FILE, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=HEADERS)
                writer.writeheader()

                print("📡 Listening for AIS messages...")

                # Stream and filter PositionReport messages
                async for message_json in websocket:
                    try:
                        message = json.loads(message_json)
                        if message.get("MessageType") != "PositionReport":
                            continue

                        msg = message["Message"]["PositionReport"]
                        meta = message.get("MetaData", {})

                        row = {
                            "timestamp": meta.get("time_utc", datetime.utcnow().isoformat()),
                            "mmsi": meta.get("MMSI", msg.get("UserID")),
                            "latitude": msg.get("Latitude"),
                            "longitude": msg.get("Longitude"),
                            "sog": msg.get("Sog"),
                            "cog": msg.get("Cog"),
                            "true_heading": msg.get("TrueHeading"),
                            "navigational_status": msg.get("NavigationalStatus")
                        }

                        writer.writerow(row)
                        print("✅ Saved AIS message:", row)

                    except Exception as msg_err:
                        print("⚠️ Message skipped:", msg_err)

    except Exception as e:
        print("❌ Connection error:", e)

# 🚀 Run script
if __name__ == "__main__":
    asyncio.run(connect_and_stream())
