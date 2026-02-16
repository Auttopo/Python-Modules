import sys

if __name__ == "__main__":
    try:
        sys.argv[1]
    except Exception:
        print("no argument gived")
    else:
        print(f"total arguments given: {len(sys.argv) - 1}")
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print(f"arg {i} : {arg}")
