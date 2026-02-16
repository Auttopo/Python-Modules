
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    target = "new_discovery.txt"
    print("Initializing new storage unit:", target)
    try:
        with open(target, "w") as file_w:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            file_w.write(
                        "[ENTRY 001] New quantum algorithm discovered\n\
[ENTRY 002] Efficiency increased by 347%\n\
[ENTRY 003] Archived by Data Archivist trainee")
            print("[ENTRY 001] New quantum algorithm discovered")
            print("[ENTRY 002] Efficiency increased by 347%")
            print("[ENTRY 003] Archived by Data Archivist trainee")
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
