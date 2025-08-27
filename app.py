import websocket
import threading

SERVER_URL = "ws://localhost:8080"

def receive_messages(ws):
    """Thread to continuously receive messages"""
    while True:
        try:
            msg = ws.recv()
            if msg:
                print(f"\n{msg}\n> ", end="")
        except:
            print("\nConnection closed.")
            break

def main():
    # Connect to server
    ws = websocket.WebSocket()
    ws.connect(SERVER_URL)
    print("Connected to chat server.")

    # Start thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(ws,))
    thread.daemon = True
    thread.start()

    # First input is the username
    username = input("Enter your name: ")
    ws.send(username)

    # Chat loop
    try:
        while True:
            msg = input("> ")
            if msg.lower() in ["exit", "quit"]:
                break
            ws.send(msg)
    except KeyboardInterrupt:
        print("\nExiting chat...")

    ws.close()

if __name__ == "__main__":
    main()
