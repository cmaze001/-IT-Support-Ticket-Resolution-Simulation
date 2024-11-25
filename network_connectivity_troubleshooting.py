import os
import platform
import subprocess
import socket

def check_os():
    """Identify the operating system."""
    print("Detecting operating system...")
    os_name = platform.system()
    print(f"Operating System: {os_name}")
    return os_name

def check_ip_config():
    """Display the IP configuration."""
    print("\nChecking IP configuration...")
    if platform.system() == "Windows":
        command = "ipconfig"
    else:
        command = "ifconfig"
    os.system(command)

def test_connectivity(host="8.8.8.8"):
    """Test internet connectivity by pinging a public DNS server."""
    print("\nTesting internet connectivity...")
    try:
        response = subprocess.run(
            ["ping", "-c", "4", host] if platform.system() != "Windows" else ["ping", "-n", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if response.returncode == 0:
            print(f"Ping to {host} successful! Internet connectivity is working.")
        else:
            print(f"Ping to {host} failed. Please check your network connection.")
    except Exception as e:
        print(f"An error occurred while testing connectivity: {e}")

def resolve_dns(host="www.google.com"):
    """Verify DNS resolution for a given hostname."""
    print("\nVerifying DNS resolution...")
    try:
        ip = socket.gethostbyname(host)
        print(f"DNS resolution successful! {host} resolves to {ip}.")
    except socket.gaierror as e:
        print(f"DNS resolution failed for {host}: {e}")

def ping_gateway(gateway="192.168.1.1"):
    """Ping the default gateway to test local network connectivity."""
    print("\nPinging the gateway...")
    try:
        response = subprocess.run(
            ["ping", "-c", "4", gateway] if platform.system() != "Windows" else ["ping", "-n", "4", gateway],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if response.returncode == 0:
            print(f"Ping to gateway {gateway} successful! Local network is reachable.")
        else:
            print(f"Ping to gateway {gateway} failed. Check local network settings.")
    except Exception as e:
        print(f"An error occurred while pinging the gateway: {e}")

def main():
    print("Network Connectivity Troubleshooting Tool")
    print("-----------------------------------------")

    # Step 1: Identify the operating system
    os_name = check_os()

    # Step 2: Check IP configuration
    check_ip_config()

    # Step 3: Test internet connectivity
    test_connectivity()

    # Step 4: Verify DNS resolution
    resolve_dns()

    # Step 5: Ping the gateway
    ping_gateway()

    print("\nNetwork troubleshooting completed.")

if __name__ == "__main__":
    main()
