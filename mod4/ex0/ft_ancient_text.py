
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    data = list()
    try:
        target = "ancient_fragment.txt"
        print("Accessing Storage Vault:", target)
        with open(target, "r") as file_r:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            data.append(file_r.read())
    except Exception as e:
        print(f"Error occured : {e}")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
