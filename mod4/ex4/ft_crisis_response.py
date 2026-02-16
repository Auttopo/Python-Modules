
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    try:
        try:
            print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
            with open("lost_archive.txt", "r") as file_r:
                print(file_r.read())
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
        finally:
            print("STATUS: Crisis handled, system stable\n")

        try:
            print(
                "CRISIS ALERT: Attempting access to 'classified_data.txt'...")
            with open("classified_data.txt", "r") as file_r:
                print("SUCCESS - ```", file_r.read(), "```")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
        finally:
            print("STATUS: Crisis handled, security maintained\n")

        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file_r:
            print("SUCCESS - ```", file_r.read(), "```")

        print("\nAll crisis scenarios handled successfully. Archives secure.")
    except Exception as e:
        print(f"Unexcpected error occured: {e}")
        print("The crisis scenario not termnied normaly")
