# This script is designed to be placed in a Text DAT operator 
# in TouchDesigner and reference your WebSocket DAT (e.g., 'websocket1').

import json
from datetime import datetime


WEBSOCKET_OP_PATH = 'websocket1' 

def send_json_message(dat):
    ws_op = op(WEBSOCKET_OP_PATH)
    
    if not ws_op or ws_op.numConnections == 0:
        dat.parent().addScriptError(f"WebSocket Operator '{WEBSOCKET_OP_PATH}' not found or not connected.")
        print(f"ERROR: WebSocket Operator '{WEBSOCKET_OP_PATH}' not found or not connected.")
        return

    data_to_send = {
        "event_type": "td_update",
        "timestamp": datetime.now().isoformat(),
        "payload": {
            # Example data points you might want to send from TD
            "intensity": 0.85, 
            "color_hsv": [0.5, 1.0, 1.0], 
            "message": "Update from TouchDesigner!",
            "frame": ws_op.currentFrame 
        }
    }

    # 3. Serialize the Python dictionary into a JSON string
    try:
        json_string = json.dumps(data_to_send)
    except Exception as e:
        dat.parent().addScriptError(f"Error serializing JSON: {e}")
        print(f"Error serializing JSON: {e}")
        return

    # 4. Send the message
    ws_op.send(json_string)
    
    print(f"Sent message ({len(json_string)} bytes): {json_string[:60]}...")


# --- TOUCHDESIGNER CALLBACK STUBS (Keep for a complete DAT script) ---

def onConnect(dat):
	"""
	Called when the WebSocket is successfully connected.
	"""
	print(f"WebSocket connected to {dat.url}")
	return

def onDisconnect(dat):
	"""
	Called when the WebSocket connection is closed.
	"""
	print("WebSocket disconnected")
	return

def onReceiveText(dat, rowIndex, message):
	"""
	Called when a text message is received from the client (e.g., the React component).
	"""
	# You can add logic here to parse incoming JSON messages from React
	# Example: received_data = json.loads(message)
	print(f"Received text message: {message[:40]}...")
	return
	
def onReceiveBinary(dat, rowIndex, message):
	"""
	Called when a binary message is received.
	"""
	return
