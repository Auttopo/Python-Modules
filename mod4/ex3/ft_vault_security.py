
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM  ===\n")

    print("Initiating secure vault access...")
    try:
        target = "classified_data.txt"
        with open(target, "r") as file_r:
            print(
                "Vault connection established with failsafe protocols to:",
                target)
            print("SECURE EXTRACTION:")
            print(file_r.read())

        target = "preservation_data.txt"
        with open(target, "w") as file_w:
            print("\nSECURE PRESERVATION:")
            file_w.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
    except Exception as e:
        print(f"Error occured : {e}")
    finally:
        print("\nAll vault operations completed with maximum security.")
