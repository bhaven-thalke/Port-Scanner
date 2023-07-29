# -*- coding: utf-8 -*-

import sys
import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    try:
        print("PORT SCANNER by BHAVEN THALE")
        print("Scanning target: " + target)
        print("Time Started: " + str(datetime.now()))
        print("-" * 50)

        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit(1)

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit(1)

    except socket.error:
        print("Could not connect to the server.")
        sys.exit(1)

    print("-" * 50)
    print("Scan completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        print("Syntax: python scanner.py <target_ip_or_hostname>")
        sys.exit(1)

    target = socket.gethostbyname(sys.argv[1])
    start_port = 1
    end_port = 1024

    scan_ports(target, start_port, end_port)
