import socket

HOST = "127.0.0.1"   # Server IP (use actual IP if on another machine)
PORT = 6000
CLIENT_NAME = "Client of Tanisha Gupta"   # Change to your name

# Input with validation loop
while True:
    try:
        client_num = int(input("Enter a number between 1 and 100: ").strip())
        if 1 <= client_num <= 100:
            break
        else:
            print("❌ Please enter a valid number between 1 and 100.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Send client data
    message = f"{CLIENT_NAME}:{client_num}"
    client_socket.sendall(message.encode())

    # Receive server response
    data = client_socket.recv(1024).decode().strip()
    if not data:
        print("⚠️ No response received from server.")
        exit(0)

    server_name, server_num = data.split(":")
    server_num = int(server_num)

    total = client_num + server_num

    # Display info (client side)
    print("\n--- Client Side ---")
    print(f"Client Name   : {CLIENT_NAME}")
    print(f"Server Name   : {server_name}")
    print(f"Client Number : {client_num}")
    print(f"Server Number : {server_num}")
    print(f"Sum           : {total}")
