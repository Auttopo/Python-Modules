
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        target = "ancient_fragment.txt"
        print("Accessing Storage Vault:", target)
        with open(target, "r") as file_r:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file_r.read(), end="")
            file_r.close()
    except Exception as e:
        print(f"Error occured : {e}")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
