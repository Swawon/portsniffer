#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def port_scanner(target, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning target: {target_ip}")
        print(f"Time started: {datetime.now()}\n")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1-second timeout
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 portsniffer.py <target> <start_port> <end_port>")
        sys.exit(1)
    
    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    port_scanner(target, start_port, end_port)
