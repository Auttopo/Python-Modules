import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    try:
        sys.argv[1]
    except Exception:
        print("no argument gived")
        print("total arguments given: 1")
    else:
        print(f"total arguments given: {len(sys.argv)}")
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print(f"arg {i} : {arg}")
