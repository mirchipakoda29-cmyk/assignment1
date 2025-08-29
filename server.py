import socket

HOST = "127.0.0.1"   # Listen on localhost (change to server IP if needed)
PORT = 6000          # Port > 5000
SERVER_NAME = "Server of John Q. Smith"
SERVER_NUM = 42      # Any number between 1–100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")

        # Receive client data
        data = conn.recv(1024).decode()
        client_name, client_num = data.split(":")
        client_num = int(client_num)

        # Validate number
        if client_num < 1 or client_num > 100:
            print("Invalid number received. Closing server.")
            conn.close()
            exit(0)

        # Calculate sum
        total = client_num + SERVER_NUM

        # Display info (server side)
        print("\n--- Server Side ---")
        print(f"Client Name: {client_name}")
        print(f"Server Name: {SERVER_NAME}")
        print(f"Client Number: {client_num}")
        print(f"Server Number: {SERVER_NUM}")
        print(f"Sum: {total}")

        # Send response back
        response = f"{SERVER_NAME}:{SERVER_NUM}"
        conn.sendall(response.encode())
