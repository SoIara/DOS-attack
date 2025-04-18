import socket
import random
import time
from datetime import datetime

# Show timestamp
now = datetime.now()
print(f"Script started at: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Setup socket and data
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(1490)  # Sample data to send

# Input IP and Port for safe testing (e.g., localhost)
ip = input("Enter target IP (e.g., 127.0.0.1): ")
port = int(input("Enter target port (e.g., 9999): "))

print("\n[====================>] Sending Test UDP Packets <[====================]")
sent = 0

try:
    while sent < 100:  # Send a limited number for safety
        sock.sendto(data, (ip, port))
        sent += 1
        print(f"Sent packet {sent} to {ip}:{port}")
        time.sleep(0.1)  # Throttle to avoid flooding
except KeyboardInterrupt:
    print("\nInterrupted by user. Exiting safely.")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
    print("Socket closed.")
