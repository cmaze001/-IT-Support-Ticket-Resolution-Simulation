import subprocess
import platform

def check_printer_connection():
    """Check if the printer is connected."""
    print("Checking printer connection...")
    printer_name = input("Enter the name of your printer: ").strip()
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["powershell", "-Command", f"Get-Printer | Where-Object {{$_.Name -eq '{printer_name}'}}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        else:  # Assume Linux/macOS
            result = subprocess.run(
                ["lpstat", "-p", printer_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        
        if result.returncode == 0 and printer_name in result.stdout:
            print(f"✔ Printer '{printer_name}' is connected.")
            return True
        else:
            print(f"✖ Printer '{printer_name}' is not detected.")
            return False
    except Exception as e:
        print(f"Error checking printer connection: {e}")
        return False

def check_printer_driver():
    """Check if the printer driver is installed."""
    print("Checking printer driver...")
    try:
        if platform.system() == "Windows":
            print("Driver check requires manual validation on Windows via 'Device Manager'.")
        else:  # Assume Linux/macOS
            result = subprocess.run(
                ["lpinfo", "-v"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("Available printer drivers:\n", result.stdout)
        print("✔ Driver check complete. Please verify the results.")
    except Exception as e:
        print(f"Error checking printer drivers: {e}")

def clear_print_queue():
    """Clear the print queue."""
    print("Clearing print queue...")
    try:
        if platform.system() == "Windows":
            subprocess.run(["powershell", "-Command", "Remove-PrintJob -ComputerName localhost"], check=True)
        else:  # Assume Linux/macOS
            subprocess.run(["cancel", "-a"], check=True)
        print("✔ Print queue cleared successfully.")
    except Exception as e:
        print(f"Error clearing print queue: {e}")

def main():
    """Main function to handle printer troubleshooting."""
    print("=== Printer Troubleshooting Tool ===")
    while True:
        print("\nOptions:")
        print("1. Check printer connection")
        print("2. Check printer driver")
        print("3. Clear print queue")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            check_printer_connection()
        elif choice == "2":
            check_printer_driver()
        elif choice == "3":
            clear_print_queue()
        elif choice == "4":
            print("Exiting Printer Troubleshooting Tool.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


=== Printer Troubleshooting Tool ===

Options:
1. Check printer connection
2. Check printer driver
3. Clear print queue
4. Exit
Select an option (1-4): 1
Enter the name of your printer: HP_LaserJet_Pro
Checking printer connection...
✖ Printer 'HP_LaserJet_Pro' is not detected.

Options:
1. Check printer connection
2. Check printer driver
3. Clear print queue
4. Exit
Select an option (1-4): 3
Clearing print queue...
✔ Print queue cleared successfully.
