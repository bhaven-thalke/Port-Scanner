# Port-Scanner
The provided Python script is a straightforward yet effective port scanner designed to identify open ports on a target host. A port is a communication endpoint in a networked system, and knowing which ports are open on a target can be essential for security assessments or network diagnostics. This port scanner allows users to quickly determine the status of ports within a specified range on a given IP address or hostname.

**Key Features:**

1.Command-Line Interface: The port scanner is invoked from the command line, allowing users to pass the target IP address or hostname as a single argument when running the script.

2.Port Range: By default, the scanner examines ports within the range of 1 to 1024, which includes the well-known ports typically used by various network services. Users can adjust the range in the code to their specific needs.

3.Socket Connections: The scanner uses the Python socket module to create TCP sockets and attempt connections to the target on each port within the specified range.

4.Timeout: To avoid prolonged delays, the script sets a socket timeout of 1 second for each connection attempt. This ensures that if a port doesn't respond promptly, the script moves on to the next port.

5.Feedback and Results: The script provides informative output during the scanning process. It displays the target being scanned, the start time of the scan, and a notification for each open port it discovers.

6.Error Handling: The script includes exception handling to manage possible errors gracefully. If the user interrupts the scan, or if the target hostname cannot be resolved, or if the script cannot connect to the server, it displays appropriate error messages and exits with an error code of 1.

7.User-Friendly: The script includes usage instructions to guide users on the correct command-line syntax and ensure a smooth user experience.

Overall, this port scanner is a versatile and convenient tool for network administrators, security professionals, or anyone interested in analyzing the status of ports on a particular target. Its simplicity and effectiveness make it a valuable addition to any network-related toolkit. However, users should always exercise caution and ensure that they have the necessary permissions before scanning any target, as aggressive or unauthorized scanning may be considered malicious and lead to adverse consequences.



**Explanation: **
**1.Shebang and Encoding Declaration:**

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

These lines are used to specify the interpreter to use for running the script (in this case, Python 3) and the character encoding used in the script (UTF-8).

**2.Importing Required Modules:**

import sys
import socket
from datetime import datetime

The code imports three modules:

sys: It provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

socket: This module provides a low-level networking interface, allowing the script to create and interact with sockets.

datetime: This module allows the script to work with date and time objects, used to display the start time of the scan.

**3.Function scan_ports(target, start_port, end_port):**

This function performs the actual port scanning. It takes three arguments:

target: The IP address or hostname of the target to scan.
start_port: The starting port number of the range to scan.
end_port: The ending port number of the range to scan.


**4.Scanning Process:**

The scanning process is carried out within the scan_ports() function. It goes through each port in the specified range, creates a socket, and attempts to connect to the target's IP address and the current port using TCP (socket.SOCK_STREAM). If the connection is successful (result == 0), it means the port is open, and the script prints a message indicating that the port is open. The socket is then closed.

**5.Exception Handling:**

The code includes exception handling to gracefully handle possible errors during the scan. Specifically, it handles three types of exceptions:

KeyboardInterrupt: If the user interrupts the scan by pressing Ctrl+C, the script will catch this exception, print a message, and exit with an error code of 1.

socket.gaierror: This exception occurs when the hostname cannot be resolved. If the target hostname cannot be translated to an IP address, the script will catch this exception, print an error message, and exit with an error code of 1.

socket.error: This exception is raised when the script cannot connect to the server. If any other socket-related error occurs during the scan, the script will catch this exception, print an error message, and exit with an error code of 1.

6.Main Block:

The if __name__ == "__main__": block checks whether the script is being run directly (as opposed to being imported as a module). If it is the main script, it proceeds with the port scanning process. It checks the number of command-line arguments and prints usage instructions if the number of arguments is not 2 (i.e., the target IP address or hostname is missing). Then, it gets the target's IP address using socket.gethostbyname() and sets the port range to scan from 1 to 1024. Finally, it calls the scan_ports() function with the provided target and port range.

When you run this script from the command line and provide a valid target IP address or hostname, it will perform a port scan on that target and display any open ports found within the specified range (1 to 1024).
