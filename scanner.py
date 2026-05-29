import socket
import threading
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "=" * 60)
print(Fore.CYAN + "      Advanced Python Network Scanner")
print(Fore.CYAN + "=" * 60)


# Ask user for target
host = input(Fore.YELLOW + "Enter target IP address: ")

# Full port range
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

# Save results
results = []

print(Fore.GREEN + f"Scanning host: {host}")
print(Fore.GREEN + f"Started at: {datetime.now()}")
print(Fore.GREEN + "-" * 60)

# Service dictionary
common_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

# Scan function

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            service = common_services.get(port, "Unknown")

            print(Fore.RED + f"[OPEN] Port {port} ({service})")

            # Banner grabbing
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    print(Fore.MAGENTA + f"Banner: {banner}")
            except:
                pass

            results.append(f"Port {port} OPEN ({service})")

        sock.close()

    except Exception as e:
        print(Fore.YELLOW + f"Error scanning port {port}: {e}")

# Multi-threaded scanning
threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Save results to file
with open("scans/results.txt", "w") as file:
    file.write(f"Scan Results for {host}")
    file.write("-" * 40 + "")

    for result in results:
        file.write(result + " ")

print(Fore.CYAN + "-" * 60)
print(Fore.CYAN + "Scan complete.")
print(Fore.CYAN + "Results saved to scans/results.txt")
