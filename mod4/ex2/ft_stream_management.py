
import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    print("Input Stream active.\n")
    name = input("Enter archivist ID: ")
    report = input("Enter status report: ")

    sys.stdout.write("\n[STANDARD] Archive status from "
                     + name + ": " + report)
    sys.stderr.write("\n[ALERT] System diagnostic:\
 Communication channels verified")
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")
