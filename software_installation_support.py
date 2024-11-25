import os
import subprocess
import sys

def check_package_installed(package_name):
    """Check if a package is installed on the system."""
    print(f"Checking if {package_name} is installed...")
    try:
        result = subprocess.run(
            ["dpkg", "-s", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            print(f"✔ {package_name} is installed.")
            return True
        else:
            print(f"✖ {package_name} is not installed.")
            return False
    except Exception as e:
        print(f"Error checking package: {e}")
        return False

def install_package(package_name):
    """Install a package using the apt package manager."""
    print(f"Installing {package_name}...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
        print(f"✔ {package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def upgrade_package(package_name):
    """Upgrade a package to the latest version."""
    print(f"Upgrading {package_name}...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "--only-upgrade", "-y", package_name], check=True)
        print(f"✔ {package_name} upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading {package_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """Main function to handle user interaction and package management."""
    if os.geteuid() != 0:
        print("⚠ This script must be run with administrative privileges. Please use sudo.")
        sys.exit(1)

    print("=== Software Installation Support Tool ===")
    package_name = input("Enter the name of the package to check/install/upgrade: ").strip()

    # Check if the package is installed
    if check_package_installed(package_name):
        action = input(f"Would you like to upgrade {package_name}? (yes/no): ").strip().lower()
        if action == "yes":
            upgrade_package(package_name)
        else:
            print(f"No action taken for {package_name}.")
    else:
        action = input(f"{package_name} is not installed. Would you like to install it? (yes/no): ").strip().lower()
        if action == "yes":
            install_package(package_name)
        else:
            print(f"No action taken for {package_name}.")

    print("=== Script Execution Complete ===")

if __name__ == "__main__":
    main()
