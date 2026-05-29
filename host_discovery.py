import os

network = input("Enter network (example 192.168.56): ")

print(f"Scanning network {network}.0/24")

for host in range(1, 255):
    ip = f"{network}.{host}"

    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    if response == 0:
        print(f"[ACTIVE] {ip}")
